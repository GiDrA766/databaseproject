from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apiv1.customer.schemas import Customer, CustomerWithOrders
from db.models import db_helper
from requests.dependency import get_filter
from requests.functions import get_customer_by_attributes, get_customer_with_his_orders

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
