from pydantic import BaseModel
from typing import Optional

class Role(BaseModel):
    name: str
