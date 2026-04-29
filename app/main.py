from contextlib import asynccontextmanager
from fastapi import FastAPI
from database.base import Base
from database.session import engine
from routers.users import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Usuarios y Vehículos: Async, API",
    description="TechTest: FastAPI, Pydantic, SQLAlchemy y Docker",
    version="1.1.1",
    lifespan=lifespan
)

app.include_router(user_router)