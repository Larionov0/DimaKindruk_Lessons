from .functions import create_keyboard, find_lobby_by_id


class Router:
    def __init__(self, bot):
        self.bot = bot

    def answer_to_update(self, update, user):
        text = self.bot.get_message_from_update(update)['text']
        user.next_message_handler(user, text)

    def start_handler(self, user, text):
        self.registration_menu(user)

    def registration_menu(self, user):
        self.bot.send_message_to_user(user, 'Ласкаво просимо:)\n'
                                        'Для початку введіть свій нікнейм.')
        user.next_message_handler = self.registration_menu_handler

    def registration_menu_handler(self, user, text):
        user.username = text
        self.bot.send_message_to_user(user, 'Ви успішно зареєстровані!')
        self.main_menu(user)

    def main_menu(self, user):
        text = '---= Головне меню =---\n' \
               f'{user.username} ({user.status})'
        keyboard = create_keyboard([
            ['Грати', "Магазин"],
            ["Аккаунт", "Начхати"]
        ])
        self.bot.send_message_to_user(user, text, keyboard)
        user.next_message_handler = self.main_menu_handler

    def main_menu_handler(self, user, text):
        if text == 'Грати':
            self.game_menu(user)
        elif text == 'Магазин':
            self.store_menu(user)
        elif text == 'Аккаунт':
            self.account_menu(user)
        elif text == 'Начхати':
            self.bot.send_message_to_user(user, 'АПЧХІ')

    def game_menu(self, user):
        text = '---= Гра =---\n'
        keyboard = create_keyboard([
            ['Створити лоббі', 'Пошук лоббі'],
            ['Назад']
        ])
        self.bot.send_message_to_user(user, text, keyboard)
        user.next_message_handler = self.game_menu_handler

    def game_menu_handler(self, user, text):
        if text == 'Пошук лоббі':
            self.lobbies_menu(user)
        elif text == 'Назад':
            self.main_menu(user)

    def lobbies_menu(self, user):
        text = '---= Доступні лоббі: =---\n'
        text += '0 - назад\n'
        for lobby in self.bot.lobbies:
            text += f"{lobby}\n"
        self.bot.send_message_to_user(user, text)
        user.next_message_handler = self.lobbies_menu_handler

    def lobbies_menu_handler(self, user, text):
        lobby = find_lobby_by_id(self.bot.lobbies, int(text))
        if lobby:
            self.bot.send_message_to_user(user, 'Користувач доданий в лоббі')
            lobby.add_player(user)
        else:
            self.bot.send_message_to_user(user, 'Такого лоббі немає')

    def store_menu(self, user):
        text = '--= Магазин =--\n' \
               '0 - назад\n' \
               '1 - статус бронза (10 монет)\n' \
               '2 - статус золото (20 монет)\n' \
               '3 - статус платина (30 монет)\n'
        self.bot.send_message_to_user(user, text)
        user.next_message_handler = self.store_menu_handler

    def store_menu_handler(self, user, text):
        if text == '0':
            self.main_menu(user)
        elif text == '1':
            if user.money >= 10:
                user.money -= 10
                user.status = 'бронза'
                self.bot.send_message_to_user(user, 'Статус змінено')
                self.main_menu(user)
            else:
                self.bot.send_message_to_user(user, 'Не вистачає коштів :(')
                self.store_menu(user)
        elif text == '2':
            pass
        elif text == '3':
            pass
        else:
            pass

    def account_menu(self, user):
        text = '--= Меню аккаунта =--\n' \
               '0 - назад\n' \
               '1 - змінити нікнейм\n' \
               '2 - видалити акаунт'
        self.bot.send_message_to_user(user, text)
        user.next_message_handler = self.account_menu_handler

    def account_menu_handler(self, user, text):
        if text == '0':
            self.main_menu(user)

        elif text == '1':
            self.bot.send_message_to_user(user, 'Окей, введіть новий нікнейм: ')
            user.next_message_handler = self.new_username_handler

        elif text == '2':
            pass

    def new_username_handler(self, user, text):
        user.username = text
        self.bot.send_message_to_user(user, 'Нікнейм оновлено!')
        self.main_menu(user)

