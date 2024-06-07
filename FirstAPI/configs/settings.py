from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default = "postgresql+asyncpg://first:first@localhost/first")

settings = Settings()