from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')
    DATABASE_URL: str

    JWT_SECRET: str
    JWT_EXP: int = 5

    # CORS_ORIGINS: list[str]
    # CORS_HEADERS: list[str]

    APP_VERSION: str = "1"







settings = Config()
