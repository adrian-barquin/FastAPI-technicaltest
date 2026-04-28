from fastapi import FastAPI
from app.database.base import Base
from app.database.session import engine
from app.routers.users import router as user_router

app = FastAPI(
    title="Usuarios y Vehículos: Async, API",
    description="TechTest FastAPI, Pydantic y SQLAlchemy",
    version="1.0.0"
)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(user_router)