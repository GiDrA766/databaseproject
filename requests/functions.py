from operator import and_

from fastapi import HTTPException
from typing import List, Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette.status import HTTP_404_NOT_FOUND

from db.models import Customer, Dish


async def get_customer_by_attributes(
    session: AsyncSession,
    where_filter=None,
) -> List[Customer]:
    if where_filter is not None:
        stmt = select(Customer).where(where_filter).order_by(Customer._id_)
    else:
        stmt = select(Customer)
    result = await session.scalars(stmt)
    return list(result.all())


async def get_customer_with_his_orders(
    customer_id: int, session: AsyncSession
) -> Optional[Customer]:
    result = await session.execute(
        select(Customer)
        .options(selectinload(Customer.orders))  # Eager load orders
        .where(Customer._id_ == customer_id)
    )
    customer = result.scalar_one_or_none()
    if customer:
        return customer
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"Customer with id {customer_id} not found",
    )


async def update_dish_price(
    session: AsyncSession,
    target_dish_category: str,
    price_threshold: float,
) -> List[Dish]:
    """Increment the price of dishes in a specific category
    if their current price meets or exceeds a given threshold.

    Args:
        session (AsyncSession): The database session to execute the query.
        target_dish_category (str): The category of dishes to update.
        price_threshold (float): The price threshold for updating dishes.
    """
    # Build update query
    select_query = select(Dish._id_).where(
        and_(
            Dish.dish_category == target_dish_category,
            Dish.dish_price <= price_threshold,  # Account for the increment
        )
    )
    result = await session.scalars(select_query)
    updating_dishes_id = result.all()

    query = (
        update(Dish)
        .where(
            and_(
                Dish.dish_category == target_dish_category,
                Dish.dish_price <= price_threshold,
            )
        )
        .values(dish_price=Dish.dish_price + 1)  # Increment price by 1
    )
    await session.execute(query)
    await session.commit()
    # Fetch updated dishes
    updated_dishes = await session.scalars(
        select(Dish).where(Dish._id_.in_(updating_dishes_id))
    )
    if len(list(updated_dishes)) > 0:
        return list(updated_dishes)

    raise HTTPException(status_code=404, detail="No dishes were updated.")
