from fastapi import APIRouter
from .searching import router as searching_router

router = APIRouter()
router.include_router(searching_router)
