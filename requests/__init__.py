from fastapi import APIRouter
from .views import router as request_router


router = APIRouter()
router.include_router(request_router, tags=["requests"])
