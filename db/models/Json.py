import json

from sqlalchemy import Column, Integer, JSON, Index, text
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from db.models import BASE


class JsonTable(BASE):
    __tablename__ = "json_orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    data: Mapped[json] = Column(JSON, nullable=False)

    __table_args__ = (
        Index(
            "json_orders_data_gin_trgm_idx",
            text("data::TEXT"),  # Преобразование JSON в текст
            postgresql_using="gin",
            postgresql_ops={"data": "gin_trgm_ops"},
        ),
    )
