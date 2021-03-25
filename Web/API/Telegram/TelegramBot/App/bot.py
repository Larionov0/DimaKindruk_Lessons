import requests
import time
from typing import List, Optional
from .globals import BASE_URL, TOKEN
from .classes.user import User
from .functions import find_user_by_chat_id
from .router import Router
from .classes.lobby import Lobby


class Bot:
    def __init__(self, token=TOKEN):
        self.token = token
        self.url = f'{BASE_URL}/bot{token}'
        self.last_update_id: int = 0
        self.router = Router(self)

        self.users: List[User] = []
        self.lobbies = [
            Lobby(self, 1, 'Base lobby UA', [], players_needed=4),
            Lobby(self, 2, 'Dop lobby UA', [])
        ]

    def get_updates(self):
        response = requests.get(f'{self.url}/getUpdates?offset={self.last_update_id + 1}')
        dct = response.json()
        return dct['result']

    def send_message(self, chat_id, text, keyboard=None):
        """
        keyboard: json str
        """
        if keyboard:
            requests.get(f'{self.url}/sendMessage?chat_id={chat_id}&text={text}&reply_markup={keyboard}')
        else:
            keyboard = '{"remove_keyboard": true}'
            requests.get(f'{self.url}/sendMessage?chat_id={chat_id}&text={text}&reply_markup={keyboard}')

    def send_message_to_user(self, user, text, keyboard=None):
        self.send_message(user.chat_id, text, keyboard)

    def run(self):
        print('Start')
        while True:
            updates = self.get_updates()

            for update in updates:
                if 'message' in update and 'text' in update['message']:
                    user = self.identify_user(update)
                    self.router.answer_to_update(update, user)
                    self.last_update_id = update["update_id"]
            time.sleep(0.3)

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
            user.next_message_handler = self.router.start_handler
            self.users.append(user)
        return user
