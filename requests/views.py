from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apiv1.customer.schemas import Customer
from db.models import db_helper
from requests.dependency import get_filter
from requests.functions import get_customer_by_attributes

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
