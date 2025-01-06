from apiv1.customer.views import router as customer_router
from apiv1.dish.views import router as dish_router
from apiv1.order.views import router as order_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(customer_router, prefix="/customer")
router.include_router(dish_router, prefix="/dish")
router.include_router(order_router, prefix="/order")
