import requests
import json
import time
from typing import List, Optional
from datetime import datetime

TOKEN = '1572882836:AAGMXBmInazcfXSAIxfIqNwy0zrXF0aGxJY'
BASE_URL = 'https://api.telegram.org'
URL = f'{BASE_URL}/bot{TOKEN}'


def print_struct(struct):
    print(json.dumps(struct, indent=4))


def find_user_by_chat_id(users, chat_id):
    """
    return:
        User if founded
        None if not
    """
    for user in users:
        if user.chat_id == chat_id:
            return user
    return None


def get_exchange_rate(date, currency_name):
    """
    return: int - ціна валюти, якщо все ок
    False - якщо валюта не знайдена
    """
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


class User:
    def __init__(self, chat_id, username):
        self.chat_id = chat_id
        self.username = username

    def send_message_to_me(self, bot, text):
        bot.send_message(self.chat_id, text)


class Bot:
    def __init__(self, token=TOKEN):
        self.token = token
        self.url = f'{BASE_URL}/bot{token}'
        self.last_update_id: int = 0
        self.users: List[User] = []

    def get_updates(self):
        response = requests.get(f'{self.url}/getUpdates?offset={self.last_update_id + 1}')
        dct = response.json()
        return dct['result']

    def send_message(self, chat_id, text):
        requests.get(f'{self.url}/sendMessage?chat_id={chat_id}&text={text}')

    def send_message_to_user(self, user, text):
        self.send_message(user.chat_id, text)

    def run(self):
        print('Start')
        while True:
            updates = self.get_updates()
            for update in updates:
                user = self.identify_user(update)
                self.answer_to_update(update, user)
                self.last_update_id = update["update_id"]
            time.sleep(0.5)

    def get_message_from_update(self, update):
        if 'message' in update:
            return update['message']
        elif 'edited_message' in update:
            return update['edited_message']

    def identify_user(self, update):
        """
        Метод для ідентифікації користувача зі списку усіх користувачів.
        Тобто шукаємо юзера по списку юзерів за chat_id.

        Якщо користувач не був знайдений у списку, то створюємо його і додаємо в список.
        Першою менюшкою нового користувача має бути реєстрація.

        return:
        User
        """
        chat_id = self.get_message_from_update(update)['chat']['id']
        user = find_user_by_chat_id(self.users, chat_id)
        if user is None:
            user = User(chat_id, f'Новачок {chat_id}')
            self.users.append(user)
        return user

    def answer_to_update(self, update, user):
        """
        /get_currency EUR   -> 34.213
        """
        text = self.get_message_from_update(update)['text']

        if not text[0] == '/':
            self.send_message_to_user(user, 'Бот поки працює лише з командами')
            return

        line_list = text.split()
        command = line_list[0]

        if command == '/get_currency':
            if len(line_list) != 2:
                self.send_message_to_user(user, 'Невірна кількість аргументів')
                return

            date = datetime.now().date()
            price = get_exchange_rate(f'{date.day}.{date.month}.{date.year}', line_list[1])
            if price is not False:
                self.send_message_to_user(user, f'Ціна {line_list[1]} : {price}')
            else:
                self.send_message_to_user(user, 'Такої валюти не знайдено')

        elif command == '/lol':
            pass
        elif command == '/start':
            self.send_message_to_user(user, 'Привіт!')
        else:
            self.send_message_to_user(user, 'Такої команди немає')

    def registration(self):
        pass


bot = Bot()
bot.run()
