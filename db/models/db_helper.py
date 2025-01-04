from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.engine.url import URL
from db.config import connect_to_base


class DataBaseHelper:
    def __init__(self, url: URL, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, expire_on_commit=False, autoflush=False, autocommit=False
        )


db_helper = DataBaseHelper(
    connect_to_base(),
    True,
)
