from pydantic import BaseSettings


class ClassConfig(BaseSettings):
    start: int
    end: int
    interval: int

    class Config:
        env_file = ".env"
        env_prefix = "class_"


class_config = ClassConfig()
