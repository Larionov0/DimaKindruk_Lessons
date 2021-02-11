import requests
import json


def print_structure(struct):
    print(json.dumps(struct, indent=4))


url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=15.12.2020'
print_structure(requests.get(url).json())
