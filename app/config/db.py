from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.config.settings import settings

engine = create_async_engine(settings.ASYNC_DATABASE_URL, echo=False)

AsyncSession = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


async def get_postgresql_db():
    async with AsyncSession() as session:
        yield session
