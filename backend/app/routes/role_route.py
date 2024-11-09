from fastapi import APIRouter
from typing import List
from app.models.role import Role
from app.config.database import db

router = APIRouter()

@router.post("/roles", response_model=Role)
async def create_role(role: Role):
    result = await db["roles"].insert_one(role.dict())
    role.id = str(result.inserted_id)
    return role

@router.get("/roles", response_model=List[Role])
async def get_roles():
    roles = await db["roles"].find().to_list(1000)
    return [Role(**role) for role in roles]
