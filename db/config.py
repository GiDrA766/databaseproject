from dotenv import dotenv_values
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


def connect_to_base() -> URL:
    config = dotenv_values()
    session_url = URL.create(
        drivername="postgresql+asyncpg",  # Use asyncpg for async PostgreSQL interaction
        username=config.get("BASE_USER"),  # e.g., config["POSTGRES_USER"]
        password=config.get("BASE_PASSWORD"),
        host=config.get("BASE_HOST"),
        port=config.get("BASE_PORT"),
        database=config.get("BASE_DB"),
    )
    return session_url
