from sqlalchemy import cast
from fastapi import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import db_helper, JsonTable

router = APIRouter()


@router.get("/searching", tags=["searching"])
async def search_orders(
    regex: str, session: AsyncSession = Depends(db_helper.session_dependency)
):
    try:
        # Создаем запрос с использованием SQLAlchemy ORM
        query = select(JsonTable).where(
            cast(JsonTable.data, String).op("~")(regex)
        )  # Преобразуем JSON -> TEXT -> Используем регулярное выражение

        # Выполняем запрос
        result = await session.execute(query)
        rows = result.scalars().all()

        # Возвращаем результат
        return {"results": [row.__dict__ for row in rows]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
