from functools import wraps

from flask import request

from config.logger import logger


def auditing_request(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        logger.info("\n")
        logger.info("Request auditing:")
        logger.info('?'.join([request.base_url, request.query_string.decode('utf-8')]))
        logger.info(f"Query parameters: {dict(request.values)}")
        response = func(*args, **kwargs)
        logger.info("\n")
        logger.info("Response auditing:")
        if response.is_json:
            logger.info(response.get_json())
        else:
            logger.info(response.get_data().decode('utf-8'))
        return response

    return wrapped
