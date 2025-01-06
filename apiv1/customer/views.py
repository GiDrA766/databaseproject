from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from . import crud
from .schemas import Customer, CreateCustomer, UpdateCustomer, PartialUpdateCustomer
from db.models import db_helper
from .dependencies import get_customer_by_id

router = APIRouter(tags=["Customer"])


@router.get("/", response_model=list[Customer])
async def get_all_customers(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> list[Customer]:
    return await crud.get_customers(session=session)


@router.get("/{customer_id}/", response_model=Customer)
async def get_specific_customer(
    customer: Customer = Depends(get_customer_by_id),
) -> Customer:
    return customer


@router.post(
    "/",
    response_model=Customer,
)
async def create_customer(
    customer_in: CreateCustomer,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Customer:
    return await crud.create_customer(session=session, creating_customer=customer_in)


@router.put("/{customer_id}/", response_model=Customer)
async def update_customer(
    customer_update: UpdateCustomer,
    customer: Customer = Depends(get_customer_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Customer:
    return await crud.update_customer(
        session=session,
        customer=customer,
        customer_update=customer_update,
    )


@router.patch("/{customer_id}/", response_model=Customer)
async def partial_update_customer(
    customer_update: PartialUpdateCustomer,
    customer: Customer = Depends(get_customer_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Customer:
    return await crud.update_customer(
        session=session,
        customer=customer,
        customer_update=customer_update,
        partial=True,
    )


@router.delete("/{customer_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(
    customer: Customer = Depends(get_customer_by_id),
    session: AsyncSession = Depends(
        db_helper.session_dependency,
    ),
) -> None:
    await crud.delete_customer(session=session, customer=customer)
    return None
