import os

import requests

from config.logger import logger
from decorators.request_decorators import timed_lru_cache


class RateHelper:
    def __init__(self, curr_from, curr_to):
        self.curr_from = curr_from
        self.curr_to = curr_to
        self.rate = 0.0

    @timed_lru_cache()
    def get_rate(self) -> float:
        url = os.path.join(os.environ["RATE_URL"], self.curr_from)
        response = requests.get(url)
        data = response.json()
        self.auditing_rate(data)
        self.rate = data["rates"][self.curr_to]
        return self.rate

    def calculate_converted_amount(self, amount: int) -> int:
        converted_float = amount * self.rate
        logger.info(f"Converted amount(raw): {converted_float}")
        fraction = int(converted_float * 100 % 100)
        logger.info(f"Converted amount fraction part: {fraction}")
        if fraction >= int(os.environ["ROUND_UP_FRACTION"]):
            logger.debug(f"Fraction part ({fraction}) is more or equal than/to "
                         f"checked value of {os.environ['ROUND_UP_FRACTION']}")
            logger.info(f"Converted amount rounded up to: {int(converted_float) + 1}")
            return int(converted_float) + 1
        logger.info(f"Converted amount rounded down to: {int(converted_float)}")
        return int(converted_float)

    def auditing_rate(self, data: dict) -> None:
        logger.info("\n")
        logger.info("Rate auditing:")
        logger.info(data["rates"])
        logger.info(f"Base currency (from): {self.curr_from}")
        logger.info(f"Convert to currency: {self.curr_to}")
        logger.info(f"Rate received from {os.environ['RATE_URL']}: "
                    f"{data['rates'][self.curr_to]} {self.curr_to} for 1 {self.curr_from}")
