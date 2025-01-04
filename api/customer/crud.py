"""
create
read
update
delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Customer
from .schemas import CreateCustomer


async def get_customers(ses: AsyncSession) -> list[Customer]:
    stmt = select(Customer).order_by(Customer.id_)
    result: Result = await ses.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_customer(ses: AsyncSession, customer_id: int) -> Customer | None:
    try:
        return await ses.get(Customer, customer_id)
    except SQLAlchemyError:
        return None


async def create_customer(
    ses: AsyncSession, creating_customer: CreateCustomer
) -> Customer | None:
    try:
        customer = Customer(**creating_customer.model_dump())
        ses.add(customer)
        await ses.commit()
        # await ses.refresh(customer)
        return customer
    except SQLAlchemyError:
        return None
