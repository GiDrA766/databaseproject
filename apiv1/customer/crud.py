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
from .schemas import CreateCustomer, UpdateCustomer, PartialUpdateCustomer


async def get_customers(session: AsyncSession) -> list[Customer]:
    stmt = select(Customer).order_by(Customer._id_)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_customer(session: AsyncSession, customer_id: int) -> Customer | None:
    try:
        return await session.get(Customer, customer_id)
    except SQLAlchemyError:
        return None


async def create_customer(
    session: AsyncSession, creating_customer: CreateCustomer
) -> Customer | None:
    try:
        customer = Customer(**creating_customer.model_dump())
        session.add(customer)
        await session.commit()
        # await session.refresh(customer)
        return customer
    except SQLAlchemyError:
        return None


async def update_customer(
    session: AsyncSession,
    customer: Customer,
    customer_update: UpdateCustomer,
    partial=False,
) -> Customer | None:
    for name, value in customer_update.model_dump(exclude_unset=partial).items():
        setattr(customer, name, value)
    await session.commit()
    await session.refresh(customer)
    return customer


async def delete_customer(session: AsyncSession, customer: Customer) -> None:
    await session.delete(customer)
    await session.commit()
