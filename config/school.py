from pydantic import BaseSettings


class School(BaseSettings):
    username: str
    password: str

    class Config:
        env_file = ".env"


school_config = School()
