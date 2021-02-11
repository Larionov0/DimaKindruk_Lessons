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
        self.next_message_handler = None

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
            user.next_message_handler = self.start_handler
            self.users.append(user)
        return user

    def answer_to_update(self, update, user):
        text = self.get_message_from_update(update)['text']
        user.next_message_handler(user, text)

    def start_handler(self, user, text):
        self.registration_menu(user)

    def registration_menu(self, user):
        self.send_message_to_user(user, 'Ласкаво просимо:)\n'
                                        'Для початку введіть свій нікнейм.')
        user.next_message_handler = self.registration_menu_handler

    def registration_menu_handler(self, user, text):
        user.username = text
        self.send_message_to_user(user, 'Ви успішно зареєстровані!')
        self.main_menu(user)

    def main_menu(self, user):
        text = '---= Головне меню =---\n' \
               f'{user.username}\n' \
               '1 - грати\n' \
               '2 - магазин\n' \
               '3 - аккаунт\n' \
               '4 - начхати'
        self.send_message_to_user(user, text)
        user.next_message_handler = self.main_menu_handler

    def main_menu_handler(self, user, text):
        if text == '1':
            pass
        elif text == '2':
            pass
        elif text == '3':
            self.account_menu(user)
        elif text == '4':
            self.send_message_to_user(user, 'АПЧХІ')

    def account_menu(self, user):
        text = '--= Меню аккаунта =--\n' \
               '1 - змінити нікнейм\n' \
               '2 - видалити акаунт'
        self.send_message_to_user(user, text)
        user.next_message_handler = self.account_menu_handler

    def account_menu_handler(self, user, text):
        if text == '1':
            self.send_message_to_user(user, 'Окей, введіть новий нікнейм: ')
            user.next_message_handler = self.new_username_handler

        elif text == '2':
            pass

    def new_username_handler(self, user, text):
        user.username = text
        self.send_message_to_user(user, 'Нікнейм оновлено!')
        self.main_menu(user)


bot = Bot()
bot.run()
