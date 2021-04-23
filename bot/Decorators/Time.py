import time

from config.bot import bot_config

def wait(secs: int = bot_config.slow_internet):
    def predicate(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            time.sleep(secs)

        return inner

    return predicate
