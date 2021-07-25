from flask import Blueprint, request, jsonify

from decorators.auditing import auditing_request
from quote.helpers import QuoteValidatorHelper, RateHelper

quote = Blueprint('quote', __name__, url_prefix='/api')


@quote.route("/quote", methods=["GET"])
@auditing_request
def get_rate():
    values = dict(request.values)
    qv = QuoteValidatorHelper(values)
    if not qv.status:
        return jsonify({"status": False, "message": qv.error_message})

    rate_helper = RateHelper(values["from_currency_code"], values["to_currency_code"])
    exchange_rate = rate_helper.get_rate()
    exchange_data = {
        "exchange_rate": exchange_rate,
        "currency_code": values["to_currency_code"],
        "amount": rate_helper.calculate_converted_amount(int(values["amount"]))
    }
    return jsonify(exchange_data)
