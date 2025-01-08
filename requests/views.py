from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apiv1.customer.schemas import Customer, CustomerWithOrders
from apiv1.dish.schemas import Dish
from apiv1.order.schemas import Order
from db.models import db_helper
from requests.dependency import get_filter
from requests.functions import (
    get_customer_by_attributes,
    get_customer_with_his_orders,
    update_dish_price,
)

router = APIRouter()


@router.get("/select_customers/", response_model=list[Customer])
async def select_customers(
    where_filter=Depends(get_filter),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    customers = await get_customer_by_attributes(
        session=session, where_filter=where_filter
    )
    return customers


@router.get(
    "/get_customer_with_orders/{customer_id}", response_model=CustomerWithOrders
)
async def get_customer_with_orders(
    customer_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await get_customer_with_his_orders(session=session, customer_id=customer_id)


@router.patch("/price_up/", response_model=list[Dish])
async def price_up(
    dish_category: str,
    price_threshold: float,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> List[Dish]:
    return await update_dish_price(
        session=session,
        target_dish_category=dish_category,
        price_threshold=price_threshold,
    )
