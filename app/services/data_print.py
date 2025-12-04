import asyncio
from sqlalchemy import select, func
from app.config.db import AsyncSession
from app.models.country import Country
from app.models.regions import Region


async def main():
    async with AsyncSession() as session:
        query = (
            select(
                Region.name.label("region_name"),
                func.sum(Country.population).label("total_population"),
                func.max(Country.population).label("max_country_population"),
                func.min(Country.population).label("min_country_population"),
                select(Country.name)
                .where(Country.region_id == Region.id)
                .order_by(Country.population.asc())
                .limit(1)
                .correlate(Region)
                .scalar_subquery()
                .label("name_min_country_population"),
                select(Country.name)
                .where(Country.region_id == Region.id)
                .order_by(Country.population.desc())
                .limit(1)
                .correlate(Region)
                .scalar_subquery()
                .label("name_max_country_population"),
            )
            .join(Country)
            .group_by(Region.id, Region.name)
            .order_by("total_population")
        )

        result = await session.execute(query)
