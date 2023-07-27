import requests
import json




base_key = "USD"
sym_key = "RUB"
amount = 100

api_key = "084870582095d66c6963c396de733e6b"

url = f'http://api.exchangeratesapi.io/v1/latest?&access_key={api_key}&base={base_key}&symbols={sym_key}'
r = requests.get(url)
resp = json.loads(r.content)
new_price = resp['rates'][sym_key] * float(amount)

print(new_price)

