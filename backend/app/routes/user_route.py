from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User
from app.services.user_service import UserService

router = APIRouter()

@router.post("/users", response_model=User)
async def create_user(user: User):
    created_user = await UserService.create_user(user)
    return created_user

@router.get("/users", response_model=List[User])
async def get_users():
    users = await UserService.get_users()
    return users