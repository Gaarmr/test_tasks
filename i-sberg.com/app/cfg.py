from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    database_url: str
    redis_url: str


settings = Settings()

