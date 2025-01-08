from fastapi import HTTPException
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette.status import HTTP_404_NOT_FOUND

from db.models import Customer


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
