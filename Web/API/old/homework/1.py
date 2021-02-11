import requests


def get_exchange_rate(date, currency_name):
    response = requests.get(
        f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    )  # Делаем запрос на API Приватбанка и получаем Response - ответ, кладем его в переменную response
    dct = response.json()
    currencies = dct['exchangeRate']

    for currency_dict in currencies:
        if 'currency' in currency_dict:
            if currency_dict['currency'] == currency_name:
                return currency_dict["saleRateNB"]

    return 'Валюти не знайдено:('


while True:
    print('--= Main menu =--')
    date = input('date: ')
    currency_name = input('currency: ')

    try:
        print(get_exchange_rate(date, currency_name))
    except Exception as error:
        print(error)
        print('Error occured:( Try again')
