from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    # if users had a relationship, it'd look like:
    # items: List[Item] = []

    class Config:
        orm_mode = True