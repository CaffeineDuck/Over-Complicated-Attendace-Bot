import time


def wait(secs: int = 2):
    def predicate(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            time.sleep(secs)

        return inner

    return predicate
