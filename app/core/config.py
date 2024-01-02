from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    sqlite_user: str = Field(..., env="SQLITE_USER")
    sqlite_password: str = Field(..., env="SQLITE_PASSWORD")
