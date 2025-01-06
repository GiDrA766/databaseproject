from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from starlette import status

from . import crud
from db.models import db_helper, Customer


async def get_customer_by_id(
    customer_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Customer:
    customer = await crud.get_customer(session=session, customer_id=customer_id)
    if customer:
        return customer
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Customer with {customer_id} not found",
    )
