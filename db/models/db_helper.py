from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from sqlalchemy.engine.url import URL
from db.config import connect_to_base


class DataBaseHelper:
    def __init__(self, url: URL, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, expire_on_commit=False, autoflush=False, autocommit=False
        )

    async def get_scoped_session(self):
        session = async_scoped_session(self.session_factory, scopefunc=current_task)
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()

    from typing import AsyncGenerator

    async def scoped_session_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        session = await self.get_scoped_session()
        yield session
        await session.close()


db_helper = DataBaseHelper(
    connect_to_base(),
    True,
)
