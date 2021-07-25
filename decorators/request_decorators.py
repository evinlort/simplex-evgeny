import datetime
import functools

from config.logger import logger


def timed_lru_cache(timeout=10):
    def wrapper(func):
        func = functools.lru_cache()(func)
        func.clean_at = datetime.datetime.now() + datetime.timedelta(seconds=float(timeout))

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if datetime.datetime.now() > func.clean_at:
                func.cache_clear()
                logger.info(f"Cache was cleared")
                logger.info(f"Executing the {func.__name__} function")
                func.clean_at = datetime.datetime.now() + datetime.timedelta(seconds=float(timeout))
            else:
                logger.info(f"Use cached return of {func.__name__} function")
            return func(*args, **kwargs)

        return wrapped

    return wrapper
