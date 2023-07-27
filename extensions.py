import json

import requests
from Config import exchanges

api_key = "084870582095d66c6963c396de733e6b"

class ApiException(Exception)
    pass

class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.Lower()]
        except KeyError:
            return ApiException(f"Валюта {base} не найдена!")
        try:
            sym_key = exchanges[sum.Lower()]
        except KeyError
            raise ApiException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise ApiException(f'Не возможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount.replace(",","."))
        except ValueError:
            raise ApiException(f'Не удалось обработать количество {amount}!')

        url = f'http://api.exchangeratesapi.io/v1/latest?&access_key={api_key}&base={base_key}&symbols={sym_key}'
        r = requests.get ( url )
        resp = json.loads ( r.content )
        new_price = resp['rates'][sym_key] * float(amount)
        return round(new_price, 2)
