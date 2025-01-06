from sqlalchemy import ForeignKey, Integer, DateTime, CheckConstraint, String
from sqlalchemy.orm import declared_attr, Mapped, mapped_column

from db.models import BASE, Dish, Customer


class Order(BASE):
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    _id_: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    dish_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Dish._id_, ondelete="CASCADE"), nullable=False
    )
    customer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Customer._id_, ondelete="CASCADE"), nullable=False
    )

    order_time: Mapped[DateTime] = mapped_column(DateTime)
    order_pay_type: Mapped[str] = mapped_column(
        String,
        CheckConstraint(
            "order_pay_type IN ('cash', 'card')", name="check_order_pay_type"
        ),
        nullable=False,
    )
