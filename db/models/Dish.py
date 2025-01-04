from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declared_attr

from db.models.modules import BASE


class Dish(BASE):

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    _id_ = Column(Integer, primary_key=True, autoincrement=True)
    dish_name = Column(String(32), nullable=False)
    car_calory = Column(Integer)
    dish_price = Column(Float)
    dish_weight = Column(Float)
    dish_category = Column(String(32))
