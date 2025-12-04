import asyncio
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from app.config.db import AsyncSession
from app.models.country import Country
from app.models.regions import Region
from app.parsers.wiki_parser import WikiParser


class DataSaver:
    async def get_or_create_region(self, session, region_name: str) -> Region:
        stmt = select(Region).where(Region.name == region_name)
        region = await session.scalar(stmt)
        if region is None:
            region = Region(name=region_name)
            session.add(region)
            await session.flush()
        return region

    async def save_to_db(self, data: list[dict]):
        async with AsyncSession() as session:
            for item in data:
                region = await self.get_or_create_region(session, item["region"])

                stmt = (
                    insert(Country)
                    .values(
                        name=item["country"],
                        population=item["population"],
                        region_id=region.id,
                    )
                    .on_conflict_do_update(
                        index_elements=["name"],
                        set_={"population": item["population"], "region_id": region.id},
                    )
                )

                await session.execute(stmt)

            await session.commit()

        print("Data saved to database")


async def main():
    parser = WikiParser()
    saver = DataSaver()

    data = await parser.parse()
    await saver.save_to_db(data)


if __name__ == "__main__":
    asyncio.run(main())
