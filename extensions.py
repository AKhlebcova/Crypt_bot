import requests
import json


class Currency:
    def __init__(self, base, quote, amount: float):
        self.base = base
        self.quote = quote
        self.amount = amount

    def get_price(self):
        req = requests.get(
            'https://min-api.cryptocompare.com/data/price?fsym=' + self.base + '&tsyms=' + self.quote).content
        return json.loads(req)[self.quote] * self.amount


class APIException(Exception):
    def __init__(self, ex_message: str):
        self.ex_message = ex_message
