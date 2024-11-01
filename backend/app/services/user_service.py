from typing import List
from app.models.user import User
from app.config.database import db
from bson import ObjectId
import bcrypt

class UserService:
    @staticmethod
    async def create_user(user: User) -> User:
        user_dict = user.dict()
        user_dict["hashed_password"] = bcrypt.hashpw(user.hashed_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        result = await db["users"].insert_one(user_dict)
        user.id = str(result.inserted_id)
        return user

    @staticmethod
    async def get_users() -> List[User]:
        users = await db["users"].find().to_list(1000)
        return [User(**user) for user in users]