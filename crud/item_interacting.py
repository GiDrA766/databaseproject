from typing import Annotated

from fastapi import Path, APIRouter
from data.items import items

read_router = APIRouter(prefix="/items")


@read_router.get("/{item_id}")
async def read_item(item_id: Annotated[int, Path(ge=1, le=1_000_000)]):
    if item_id in items.keys():
        return items[item_id]
    else:
        return {"message": "Item not found"}
