from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DATABASE_URL: PostgresDsn

    JWT_SECRET: str
    JWT_EXP: int = 5

    CORS_ORIGINS: list[str]
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1"


settings = Config()
