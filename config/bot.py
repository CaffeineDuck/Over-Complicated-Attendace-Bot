from pydantic import BaseSettings


class BotConfig(BaseSettings):
    chromedriver: str
    slow_internet: int

    class Config:
        env_file = ".env"


bot_config = BotConfig()
