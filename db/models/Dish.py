from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import declared_attr, Mapped, mapped_column

from db.models.modules import BASE


class Dish(BASE):

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    _id_: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    dish_name: Mapped[str] = mapped_column(String(32), nullable=False)
    dish_calory: Mapped[int] = mapped_column(Integer)
    dish_price: Mapped[float] = mapped_column(Float)
    dish_weight: Mapped[float] = mapped_column(Float)
    dish_category: Mapped[str] = mapped_column(String(32))

    @property
    def id_(self):
        return self._id_
