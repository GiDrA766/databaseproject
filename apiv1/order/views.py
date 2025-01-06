from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apiv1.order.crud import get_all_orders, creating_order
from apiv1.order.schemas import Order, OrderCreate
from db.models import db_helper

router = APIRouter(tags=["Order"])


@router.get("/", response_model=list[Order])
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    dishes = await get_all_orders(session=session)
    return dishes


@router.get("/{order_id}/", response_model=Order | None)
async def get_order(
    order_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Order | None:
    order = await get_order(session=session, order_id=order_id)
    if order:
        return order
    return None


@router.post("/", response_model=Order)
async def create_order(
    order_in: OrderCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await creating_order(session=session, order_in=order_in)
