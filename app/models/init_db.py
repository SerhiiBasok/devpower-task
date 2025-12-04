import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.models.base import Base
from app.config.settings import settings
from app.models.regions import Region
from app.models.country import Country


async def init_db():
    engine = create_async_engine(settings.ASYNC_DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
    print("All tables created!")


if __name__ == "__main__":
    asyncio.run(init_db())
