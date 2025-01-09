from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.config import settings
from apiv1 import router as router_v1
from requests import router
import uvicorn
from optional import router as router_optional


@asynccontextmanager
async def lifespan(app: FastAPI):
    # try:
    #     async with db_helper.engine.begin() as conn:
    #         await conn.run_sync(BASE.metadata.create_all)
    #     yield
    # except Exception as e:
    #     # Log the exception or gracefully handle it
    #     print(f"Error during startup: {e}")
    #     raise
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)

app.include_router(router, prefix=settings.requests_prefix)
app.include_router(router_optional)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
