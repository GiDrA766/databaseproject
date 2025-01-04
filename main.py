import asyncio
from contextlib import asynccontextmanager
from db.models import BASE, db_helper
from fastapi import FastAPI, Path
from crud.item_interacting import read_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with db_helper.engine.begin() as conn:
            await conn.run_sync(BASE.metadata.create_all)
        yield
    except Exception as e:
        # Log the exception or gracefully handle it
        print(f"Error during startup: {e}")
        raise


app = FastAPI(lifespan=lifespan)
app.include_router(read_router, tags=["reading"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
