import requests
import json
from config import keys

class Exceptions(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(val1: str, val2: str, amount: str):
        if val1 == val2:
            raise Exceptions("Вы вводите две одинаковые валюты, в таких случаях курс всегда равен 1")

        try:
            key_val1 = keys[val1]
        except KeyError:
            raise Exceptions(f"Не удалось обработать валюту {val1}")

        try:
            key_val2 = keys[val2]
        except KeyError:
            raise Exceptions(f"Не удалось обработать валюту {val2}")

        try:
            amount = float(amount)
        except ValueError:
            raise Exceptions(f"Не удалось обработать количество {amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={key_val1}&tsyms={key_val2}')
        sum = json.loads(r.content)[keys[val2]]

        return sum