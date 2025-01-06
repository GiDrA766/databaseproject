from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from apiv1.dish.schemas import DishCreate, DishUpdate
from db.models import Dish


async def get_dishes(session: AsyncSession) -> list[Dish]:
    stmt = select(Dish).order_by(Dish._id_)
    result = await session.execute(stmt)
    dishes = result.scalars().all()
    return list(dishes)


async def get_dish(session: AsyncSession, dish_id: int) -> Dish | None:
    try:
        return await session.get(Dish, dish_id)
    except SQLAlchemyError:
        return


async def creating_dish(session: AsyncSession, crt_dish: DishCreate) -> Dish | None:
    try:
        dish = Dish(**crt_dish.model_dump())
        session.add(dish)
        await session.commit()
        await session.refresh(dish)
        return dish
    except SQLAlchemyError:
        return None


async def update_dish(
    session: AsyncSession,
    dish: Dish,
    dish_update: DishUpdate,
    partial=False,
) -> Dish | None:
    for name, value in dish_update.model_dump(exclude_unset=partial).items():
        setattr(dish, name, value)
    await session.commit()
    await session.refresh(dish)
    return dish


async def delete_dish(session: AsyncSession, dish: Dish):
    await session.delete(dish)
    await session.commit()
