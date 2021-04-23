from pydantic import BaseSettings

class BotConfig(BaseSettings):
    chromedriver: str

    class Config:
        env_file = '.env'

bot_config = BotConfig()