from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    ADMIN_ID: int

    class Config:
        env_file = ".env"


settings = Settings()
