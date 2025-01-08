from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from apiv1 import order
from apiv1.order.crud import get_all_orders, creating_order
from apiv1.order.schemas import Order, OrderCreate, UpdateOrder
from db.models import db_helper

router = APIRouter(tags=["Order"])


@router.get("/", response_model=list[Order])
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Order]:
    dishes = await get_all_orders(session=session)
    return dishes


@router.get("/{order_id}/", response_model=Optional[Order])
async def get_order(
    order_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Optional[Order]:
    order = await get_order(session=session, order_id=order_id)
    if order:
        return order
    return None


@router.post("/", response_model=Order)
async def create_order(
    order_in: OrderCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Order:
    return await creating_order(session=session, order_in=order_in)


@router.put("/{order_id}/", response_model=Order)
async def update_order(
    order_update: UpdateOrder,
    order: Order = Depends(get_order),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Order:
    return await update_order(
        session=session,
        order=order,
        order_update=order_update,
    )


@router.patch("/{order_id}/", response_model=Order)
async def partial_update_order(
    order_update: UpdateOrder,
    order: Order = Depends(get_order),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_order(
        session=session,
        order=order,
        order_update=order_update,
        partial=True,
    )


@router.delete("/{order_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
    order: Order = Depends(get_order),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await delete_order(session=session, order=order)
    return None
