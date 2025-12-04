import asyncio
import asyncpg
from app.config.settings import settings


async def test():
    conn = await asyncpg.connect(
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        database=settings.POSTGRES_DB,
    )
    print(await conn.fetch("SELECT 1"))
    await conn.close()


asyncio.run(test())
