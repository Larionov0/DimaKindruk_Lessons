import requests
import json


TOKEN = '1572882836:AAGMXBmInazcfXSAIxfIqNwy0zrXF0aGxJY'
BASE_URL = 'https://api.telegram.org'
URL = f'{BASE_URL}/bot{TOKEN}'


def print_struct(struct):
    print(json.dumps(struct, indent=4))


def get_updates(offset=0):
    response = requests.get(f'{URL}/getUpdates?offset={offset}')
    dct = response.json()
    return dct['result']


def send_message(chat_id, text):
    response = requests.get(f'{URL}/sendMessage?chat_id={chat_id}&text={text}')


print_struct(get_updates(326324025 + 1))
