from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from starlette import status

from . import crud
from db.models import db_helper, Dish


async def get_dish_by_id(
    dish_in: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Dish:
    dish = await crud.get_dish(session=session, dish_id=dish_in)
    if dish:
        return dish
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Dish with {dish_in} not found",
    )
