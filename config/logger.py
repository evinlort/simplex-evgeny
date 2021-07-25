import logging
import os


class Logger:
    def __init__(self, environment=os.environ['ENVIRONMENT']):
        log_formatter = logging.Formatter("%(asctime)s - Proc: %(process)d - [%(levelname)8s]  %(message)s")
        main_logger = logging.getLogger()
        level = logging.INFO
        if environment == "develop" or os.environ['DEBUG']:
            level = logging.DEBUG
        main_logger.setLevel(level)

        file_handler = logging.FileHandler(os.environ['LOG_PATH'])
        file_handler.setFormatter(log_formatter)
        main_logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        main_logger.addHandler(console_handler)

        self.logger = main_logger


logger = Logger().logger
