from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from . import crud
from .dependencies import get_dish_by_id
from .crud import get_dishes, creating_dish
from .schemas import DishCreate, Dish, DishUpdate, PartialUpdateDish
from db.models import db_helper

router = APIRouter(tags=["Dish"])


@router.get("/", response_model=list[Dish])
async def get_all_dishes(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> list[Dish]:
    dishes = await get_dishes(session=session)
    return dishes


@router.get("/{dish_id}/", response_model=Dish)
async def get_dish(
    dish=Depends(get_dish_by_id),
) -> Dish:
    return dish


@router.post(
    "/",
    response_model=Dish,
)
async def create_dish(
    dish_in: DishCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Dish:
    return await creating_dish(session=session, crt_dish=dish_in)


@router.put("/{dish_id}/", response_model=Dish)
async def update_dish(
    dish_update: DishUpdate,
    dish: Dish = Depends(get_dish_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Dish:
    return await crud.update_dish(
        session=session,
        dish=dish,
        dish_update=dish_update,
    )


@router.patch("/{dish_id}/", response_model=Dish)
async def partial_update_dish(
    dish_update: PartialUpdateDish,
    dish=Depends(get_dish_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Dish:
    return await crud.update_dish(
        session=session,
        dish=dish,
        dish_update=dish_update,
        partial=True,
    )


@router.delete("/{dish_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dish(
    dish: Dish = Depends(get_dish_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await crud.delete_dish(session=session, dish=dish)
    return None
