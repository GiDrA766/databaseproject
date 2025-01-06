from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, date


class OrderBase(BaseModel):
    dish_id: int
    customer_id: int
    order_time: date
    order_pay_type: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    order_id: int = Field(alias="_id_")
    model_config = ConfigDict(from_attributes=True)
