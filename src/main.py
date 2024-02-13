from fastapi import FastAPI

from .auth.auth_config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserUpdate, UserCreate

app = FastAPI(title='SupreLTD')

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

