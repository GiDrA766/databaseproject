from typing import Optional

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from apiv1.order.schemas import OrderCreate, UpdateOrder
from db.models import Order


async def get_all_orders(
    session: AsyncSession, offset: int = 0, limit: int = 10
) -> list[Order]:
    stmt = select(Order).order_by(Order._id_).offset(offset=offset).limit(limit=limit)
    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)


async def get_order(session: AsyncSession, order_id: int) -> Optional[Order]:
    order = await session.get(Order, order_id)
    if order:
        return order
    return None


async def creating_order(
    session: AsyncSession, order_in: OrderCreate
) -> Optional[Order]:
    order = Order(**order_in.model_dump())
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order


async def update_order(
    session: AsyncSession, order: Order, order_update: UpdateOrder, partial=False
) -> Optional[Order]:
    for name, value in order_update.model_dump(exclude_unset=partial).items():
        setattr(order, name, value)
    await session.commit()
    await session.refresh(order)
    return order


async def delete_order(session: AsyncSession, order: Order) -> None:
    await session.delete(order)
    await session.commit()
