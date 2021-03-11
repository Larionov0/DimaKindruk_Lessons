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
               f'{user.username} ({user.status})\n' \
               '1 - грати\n' \
               '2 - магазин\n' \
               '3 - аккаунт\n' \
               '4 - начхати'
        self.bot.send_message_to_user(user, text)
        user.next_message_handler = self.main_menu_handler

    def main_menu_handler(self, user, text):
        if text == '1':
            self.game_menu(user)
        elif text == '2':
            self.store_menu(user)
        elif text == '3':
            self.account_menu(user)
        elif text == '4':
            self.bot.send_message_to_user(user, 'АПЧХІ')

    def game_menu(self, user):
        text = '---= Гра =---\n' \
               '0 - назад\n' \
               '1 - створити власне лоббі\n' \
               '2 - пошук лоббі'
        self.bot.send_message_to_user(user, text)
        user.next_message_handler = self.game_menu_handler

    def game_menu_handler(self, user, text):
        if text == '2':
            self.lobbies_menu(user)

    def lobbies_menu(self, user):
        text = '---= Доступні лоббі: =---\n'
        for lobby in self.bot.lobbies:
            text += f"{lobby.id} - {lobby.name}\n"
        self.bot.send_message_to_user(user, text)

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

