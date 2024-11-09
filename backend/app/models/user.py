from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    username: str
    email: EmailStr
    hashed_password: str
    role_id: str  # New field to reference Role