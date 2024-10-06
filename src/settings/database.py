import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")

POSTGRES_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()
async_engine = create_async_engine(url=POSTGRES_URL, echo=True)


async def init_db():
    """Create the database tables."""
    async with async_engine.begin() as conn:
        # Import User model here to ensure it's registered with Base
        from users.models import User  # noqa: F401

        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    """Dependency to provide the session object."""
    async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        yield session
