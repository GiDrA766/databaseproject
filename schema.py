from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, CheckConstraint
import database

BASE = declarative_base()

class Dish(BASE):
    __tablename__ = "Dish"
    _id_ = Column(Integer, primary_key=True, autoincrement=True)
    dish_name = Column(String(32), nullable=False)
    car_calory= Column(Integer)
    dish_price = Column(Float)
    dish_weight = Column(Float)
    dish_category = Column(String(32))

class Order(BASE):
    __tablename__ = "Order"
    _id_ = Column(Integer, primary_key=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey(Dish._id_, ondelete="CASCADE"), nullable=False)
    customer_id = Column(Integer, ForeignKey("Customer._id_", ondelete="CASCADE"), nullable=False)

    order_time = Column(DateTime)
    order_pay_type = Column(
        String,
        CheckConstraint("order_pay_type IN ('Cash', 'Card')", name="check_order_pay_type"),
        nullable=False
    )


class Customer(BASE):
   __tablename__ = "Customer"
   _id_ = Column(Integer, primary_key=True, autoincrement=True)
   customer_fullname = Column(String(80))
   customer_organization = Column(String(60))
   customer_preferences = Column(String(60))
   customer_age = Column(Integer)
   customer_weight = Column(Float)
