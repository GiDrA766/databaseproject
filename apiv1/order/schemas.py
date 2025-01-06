from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, date


class OrderBase(BaseModel):
    dish_id: int
    customer_id: int
    order_time: date
    order_pay_type: str


class OrderCreate(OrderBase):
    pass


class UpdateOrder(OrderCreate):
    pass


class PartialUpdateOrder(OrderCreate):
    dish_id: int | None = None
    customer_id: int | None = None
    order_time: date | None = None
    order_pay_type: str | None = None


class Order(OrderBase):
    order_id: int = Field(alias="_id_")
    model_config = ConfigDict(from_attributes=True)
