from pydantic import BaseModel, EmailStr
from app.schemas.vehicle import VehicleOut

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    age: int | None
    active: bool = True

class UserWithInactiveVehicles(BaseModel):
    id: int
    name: str
    email: str
    vehicles: list[VehicleOut]

    model_config= {"from_attributes": True}