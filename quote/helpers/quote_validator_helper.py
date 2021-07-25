import os
from typing import Tuple


class QuoteValidatorHelper:
    def __init__(self, values: dict):
        self.values = values
        self.status, self.error_message = self.validate_quote()

    def parameters_count_validator(self):
        return len(self.values) == 3

    def get_rate_fields_validator(self) -> bool:
        mandatory_request_fields = ["from_currency_code", "to_currency_code", "amount"]
        if not all(value in mandatory_request_fields for value in self.values):
            return False
        return True

    def currency_validator(self) -> bool:
        if self.values["from_currency_code"] not in os.environ["SUPPORTED_CURRENCIES"] or \
                self.values["to_currency_code"] not in os.environ["SUPPORTED_CURRENCIES"]:
            return False
        return True

    def amount_validator(self) -> bool:
        try:
            int(self.values["amount"])
        except ValueError:
            return False
        return True

    def validate_quote(self) -> Tuple[bool, str]:
        if self.values is None:
            return False, "Required query parameters are absent"
        if not self.parameters_count_validator():
            return False, "Wrong query parameters count"
        if not self.get_rate_fields_validator():
            return False, "Wrong query parameters"
        if not self.currency_validator():
            return False, "Wrong currency"
        if not self.amount_validator():
            return False, "Wrong amount"
        return True, ""
