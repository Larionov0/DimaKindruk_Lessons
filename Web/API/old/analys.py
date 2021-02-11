import plotly.graph_objs as go
import requests
import datetime


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

    return False


currency_name = 'RUB'

dates = []
exchange_rates = []

year = 2014
while year <= 2020:
    print(f'Оброблюється {year} рік...')
    date = f"01.01.{year}"
    rate = get_exchange_rate(date, currency_name)
    dates.append(date)
    exchange_rates.append(rate)
    year += 1

print('Оброблюється сьогоднішнє число')
date_ = datetime.datetime.now()
date = f"{date_.day}.{date_.month}.{date_.year}"
rate = get_exchange_rate(date, currency_name)
dates.append(date)
exchange_rates.append(rate)

diag = go.Bar(x=dates, y=exchange_rates, name=f'Ціни валюти {currency_name} (у грн)')
go.Figure(data=[diag]).write_html('exchange_ratesRUB.html', auto_open=True)
