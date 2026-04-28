from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.user import User
from app.models.vehicle import Vehicle
from app.schemas.user import UserCreate, UserWithInactiveVehicles
from app.core.logging import logger

from app.schemas.user import UserCreate

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate,db: AsyncSession = Depends(get_db)):
    new_user = User(**user.model_dump())
    db.add(new_user)

    await db.commit()
    await db.refresh(new_user)

    logger.info(f"Usuario creado con id {new_user.id}")
    return new_user

@router.get("active-with-inactive-vehicles", response_model=list[UserWithInactiveVehicles])
async def get_active_users_with_inactive_vehicles(db: AsyncSession = Depends(get_db)):
    stmt = (
        select(User).where(User.active.is_(True)).options(selectinload(User.vehicles.and_(Vehicle.active.is_(False))))
    )
    result = await db.execute(stmt)
    users = result.scalars().all()

    return users