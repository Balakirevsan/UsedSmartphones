from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User
from app.services.user_service import UserService

router = APIRouter()

@router.post("/users", response_model=User)
async def create_user(user: User):
    try:
        created_user = await UserService.create_user(user)
        return created_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users", response_model=List[User])
async def get_users():
    users = await UserService.get_users()
    return users

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    success = await UserService.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}