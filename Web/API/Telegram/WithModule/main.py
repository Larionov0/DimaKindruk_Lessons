import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot('1630823078:AAHuZOCepyTGEwhMKP7iugW1TBy15Z1IdDw')


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Вітаємо в нашому боті!) Як справи?')
    main_menu(message)


def main_menu(message):
    chat_id = message.chat.id
    text = '--= Головне меню =--\n'
    keyboard = ReplyKeyboardMarkup()
    keyboard.row(KeyboardButton('Играть'), KeyboardButton('Магазин'))
    keyboard.row(KeyboardButton('Аккаунт'))
    bot.send_message(chat_id, text, reply_markup=keyboard)
    bot.register_next_step_handler(message, main_menu_handler)


def main_menu_handler(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Ви вирішили пограти')
    elif message.text == 'Магазин':
        bot.send_message(message.chat.id, 'Ви вибрали магазин')
        main_menu(message)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.send_message(message.chat.id, f'{message.text}!!!')


bot.polling(none_stop=True)
