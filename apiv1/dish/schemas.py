from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict

from apiv1.order.schemas import OrderWithCustomerAndDish


class DishBase(BaseModel):
    dish_name: str
    dish_calory: int
    dish_price: float
    dish_weight: float
    dish_category: str


class DishCreate(DishBase):
    pass


class DishUpdate(DishCreate):
    pass


class PartialUpdateDish(DishCreate):
    dish_name: str | None = None
    dish_calory: int | None = None
    dish_price: float | None = None
    dish_weight: float | None = None
    dish_category: str | None = None


class Dish(DishBase):
    dish_id: int = Field(alias="_id_")
    model_config = ConfigDict(from_attributes=True)


class DishWithOrder(Dish):
    orders: list["Order"] = None


class DishWithOrderAndCustomer(Dish):
    orders: list["OrderWithCustomer"] = None


from apiv1.order.schemas import Order, OrderWithCustomer
