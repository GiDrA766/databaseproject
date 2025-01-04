from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declared_attr

from db.models import BASE


class Customer(BASE):
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    _id_ = Column(Integer, primary_key=True, autoincrement=True)
    customer_fullname = Column(String(length=60))
    customer_organization = Column(String(length=60))
    customer_preferences = Column(String(length=60))
    customer_age = Column(Integer)
    customer_weight = Column(Float)
