import requests

# https://v6.exchangerate-api.com/v6/bb2e134333b0372b457c0b73/pair/USD/UZS

API_KEY = "bb2e134333b0372b457c0b73"
FROM = "USD"
TO = "UZS"

data = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{FROM}/{TO}")
json_data = data.json()
kurs = json_data["conversion_rate"]
# print(kurs)
