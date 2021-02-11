from os import system
from msvcrt import getch
import json


def press(message):
    print(message)
    sym = getch()
    return str(sym)[2:-1]


def main_menu(users):
    while True:
        system('cls')
        print(users)
        print("--= Програма секретів =--\n"
              "1 - зареєструватися\n"
              "2 - увійти в аккаунт\n"
              "3 - вийти з програми\n")
        choice = press("Ваш варіант:")

        if choice == '1':
            registration(users)
        elif choice == '2':
            log_in(users)
        elif choice == '3':
            save(users)
            break
        else:
            pass


def input_username():
    """
    Перевіряє, чи username підходить:
    1. мінімум 4 символи
    2. тільки літери й числа й ще пара символів
    3. чи не повторюється
    :return: username
    """
    while True:
        username = input('Введіть свій логін: ')
        if len(username) < 4:
            print('Замалий')
            continue

        result = True
        for symbol in username:
            if not (symbol.isalnum() or symbol in ('_', '$', '@')):
                print("Недопустимий символ: ", symbol)
                result = False
        if not result:
            continue

        if is_username_repeats(username, users):
            print('Юзернейм повторюється')
            continue

        return username


def is_username_repeats(username, users):
    for user in users:
        if username == user['username']:
            return True
    return False


def input_password():
    while True:
        password = input("Введіть пароль: ")
        if len(password) < 6:
            print('Замалий пароль')
            continue

        return password


def registration(users):
    username = input_username()
    password = input_password()

    user = {
        'username': username,
        'password': password,
        'secrets': []
    }
    users.append(user)


def log_in(users):
    pass


def save(users, filename='data.json'):
    with open(filename, 'wt', encoding='utf-8') as file:
        string = json.dumps(users, ensure_ascii=False, indent=4)  # перетворює об'єкт (в даному випаддку список) на строку
        file.write(string)  # зберігаємо строку в файл


def load(filename='data.json'):
    with open(filename, encoding='utf-8') as file:
        string = file.read()  # Дістаємо строку з файлу (в форматі JSON) (приклад: '{"lol": 12, "kek": false, "bub": [1, 2, null]}')
    return json.loads(string)  # Повертає об'єкт, який вигружає зі строки (тільки якщо строка в форматі JSON)


users = load()
main_menu(users)
