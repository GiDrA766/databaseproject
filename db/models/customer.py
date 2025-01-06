from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import declared_attr, Mapped, mapped_column

from db.models import BASE


class Customer(BASE):
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    _id_: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    customer_fullname: Mapped[str] = mapped_column(String(length=60))
    customer_organization: Mapped[str] = mapped_column(String(length=60))
    customer_preferences: Mapped[str] = mapped_column(String(length=60))
    customer_age: Mapped[int] = mapped_column(Integer)
    customer_weight: Mapped[float] = mapped_column(Float)
