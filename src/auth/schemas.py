import uuid
from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: uuid.UUID
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    s_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    s_verified:  Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass
