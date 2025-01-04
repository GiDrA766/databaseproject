from sqlalchemy import Column, ForeignKey, Integer, DateTime, CheckConstraint, String
from sqlalchemy.orm import declared_attr

from db.models import BASE, Dish


class Order(BASE):
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    _id_ = Column(Integer, primary_key=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey(Dish._id_, ondelete="CASCADE"), nullable=False)
    customer_id = Column(
        Integer, ForeignKey("Customer._id_", ondelete="CASCADE"), nullable=False
    )

    order_time = Column(DateTime)
    order_pay_type = Column(
        String,
        CheckConstraint(
            "order_pay_type IN ('Cash', 'Card')", name="check_order_pay_type"
        ),
        nullable=False,
    )
