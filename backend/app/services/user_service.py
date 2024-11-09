from typing import List
from app.models.user import User
from app.config.database import db
from app.config.redis_config import redis_client
import bcrypt
import json
import logging

logger = logging.getLogger(__name__)

class UserService:
    @staticmethod
    async def create_user(user: User) -> User:
        user_dict = user.dict()
        user_dict["hashed_password"] = bcrypt.hashpw(user.hashed_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        result = await db["users"].insert_one(user_dict)
        user.id = str(result.inserted_id)
        # Cache the user in Redis
        redis_client.set(f"user:{user.id}", json.dumps(user_dict))
        return user

    @staticmethod
    async def get_users() -> List[User]:
        # Try to get users from cache
        cached_users = redis_client.get("users")
        if cached_users:
            logger.info("Loaded users from cache")
            return [User(**user) for user in json.loads(cached_users)]
        
        # If not in cache, get from database
        users = await db["users"].find().to_list(1000)
        user_list = [User(**user) for user in users]
        # Cache the users in Redis
        redis_client.set("users", json.dumps([user.dict() for user in user_list]))
        logger.info("Loaded users from database")
        return user_list

    @staticmethod
    async def delete_user(user_id: str) -> bool:
        result = await db["users"].delete_one({"_id": user_id})
        if result.deleted_count:
            # Remove user from cache
            redis_client.delete(f"user:{user_id}")
            # Update the cached users list
            users = await db["users"].find().to_list(1000)
            redis_client.set("users", json.dumps([user.dict() for user in users]))
            return True
        return False