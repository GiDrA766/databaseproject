"""
create
read
update
delete
"""

from typing import Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Customer
from .schemas import CreateCustomer, PartialUpdateCustomer


async def get_customers(
    session: AsyncSession, offset: int = 0, limit: int = 10
) -> list[Customer]:
    stmt = (
        select(Customer)
        .order_by(Customer._id_)
        .offset(offset=offset)
        .limit(limit=limit)
    )
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_customer(session: AsyncSession, customer_id: int) -> Optional[Customer]:
    try:
        return await session.get(Customer, customer_id)
    except SQLAlchemyError:
        return None


async def create_customer(
    session: AsyncSession, creating_customer: CreateCustomer
) -> Optional[Customer]:
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
    customer_update: PartialUpdateCustomer,
    partial=False,
) -> Optional[Customer]:
    for name, value in customer_update.model_dump(exclude_unset=partial).items():
        setattr(customer, name, value)
    await session.commit()
    await session.refresh(customer)
    return customer


async def delete_customer(session: AsyncSession, customer: Customer) -> None:
    await session.delete(customer)
    await session.commit()
