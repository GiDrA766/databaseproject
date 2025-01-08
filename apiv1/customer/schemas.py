from __future__ import annotations  # Enable forward references

from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field


class CustomerBase(BaseModel):
    customer_fullname: str
    customer_organization: str
    customer_preferences: str
    customer_age: int
    customer_weight: float


class CreateCustomer(CustomerBase):
    pass


class UpdateCustomer(CreateCustomer):
    pass


class PartialUpdateCustomer(CreateCustomer):
    customer_fullname: str | None = None
    customer_organization: str | None = None
    customer_preferences: str | None = None
    customer_age: int | None = None
    customer_weight: float | None = None


class Customer(CustomerBase):
    model_config = ConfigDict(from_attributes=True)
    customer_id: int = Field(alias="_id_")


class CustomerWithOrders(Customer):
    orders: List["Order"] = None


class CustomerWithOrdersAndDish(Customer):
    orders: List["OrderWithDish"] = None


from apiv1.order.schemas import Order, OrderWithDish  # Delayed import
