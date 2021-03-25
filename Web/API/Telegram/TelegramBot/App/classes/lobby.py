from ..functions import create_keyboard


class Lobby:
    def __init__(self, bot, id_, name, players=None, players_needed=2, creator=None):
        self.bot = bot
        self.id = id_
        self.name = name
        if players is None:
            self.players = []
        else:
            self.players = players
        self.players_needed = players_needed
        self.creator = creator

    def add_player(self, player):
        self.players.append(player)

        for player in self.players:
            self.lobby_menu(player)

        if len(self.players) == self.players_needed:
            self.start_game()

    def remove_player(self, user):
        self.players.remove(user)
        for player in self.players:
            if player is not user:
                self.lobby_menu(player)

    def start_game(self):
        for player in self.players:
            self.bot.send_message_to_user(player, 'Гра почалась')

    def lobby_menu(self, user):
        text = f'--= Ви в лоббі {self.name}\n'
        for player in self.players:
            text += f"- {player}\n"
        keyboard = create_keyboard([
            ['Вихід', 'Інфо']
        ])
        self.bot.send_message_to_user(user, text, keyboard)
        user.next_message_handler = self.lobby_menu_handler

    def lobby_menu_handler(self, user, text):
        if text == 'Вихід':
            self.remove_player(user)
            self.bot.router.main_menu(user)
        elif text == 'Інфо':
            pass

    def __str__(self):
        return f"{self.id} - {self.name}  ({len(self.players)}/{self.players_needed})"
