from itertools import product

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from . import crud
from .schemas import Customer, CreateCustomer

router = APIRouter(tags=["Customer"])


@router.get("/", response_model=list[Customer])
async def get_all_customers(session):
    return await crud.get_customers(ses=session)


@router.get("/{product_id}/", response_model=Customer)
async def get_all_customers(customer_id: int, session):
    customer = await crud.get_customer(ses=session, customer_id=customer_id)
    if customer:
        return customer
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Customer with {customer_id} not found",
    )


@router.post(
    "/",
    response_model=Customer,
)
async def create_customer(customer_in: CreateCustomer, session):
    return await crud.create_customer(ses=session, creating_customer=customer_in)
