class User:
    def __init__(self, chat_id, username):
        self.chat_id = chat_id
        self.username = username
        self.next_message_handler = None
        self.status = 'дерево'
        self.money = 10

    def send_message_to_me(self, bot, text):
        bot.send_message(self.chat_id, text)
