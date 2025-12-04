import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import OperationalError
from app.models.base import Base
from app.config.settings import settings

async def init_db():
    engine = create_async_engine(settings.ASYNC_DATABASE_URL, echo=True)
    while True:
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            break
        except OperationalError:
            print("Postgres not ready, retrying...")
            await asyncio.sleep(1)
    await engine.dispose()
    print("All tables created!")

if __name__ == "__main__":
    asyncio.run(init_db())
