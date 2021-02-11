import requests
import json


def print_structure(struct):
    print(json.dumps(struct, indent=4))


def main_menu():
    city = 'Kyiv'
    while True:
        print('--= Погода зараз =--')
        print(f"Місто: {city}")
        print('1 - дізнатись погоду')
        print('2 - змінити місто')
        print('0 - вихід з програми')

        choice = input('Ваш вибір: ')

        if choice == '1':
            url = f'http://api.openweathermap.org/data/2.5/weather' \
                  f'?q={city}' \
                  f'&appid=cb5c7fc26a28e83605cff4b8efb1b85f' \
                  f'&units=metric'

            try:
                dct = requests.get(url).json()
                text = '---= Погода =---\n' \
                       f'Головна: {dct["weather"][0]["main"]}\n' \
                       f'Температура: {dct["main"]["temp"]}\n' \
                       f'Відчувається як: {dct["main"]["feels_like"]}\n' \
                       f'Швидкість вітру: {dct["wind"]["speed"]}'
                print(text)
            except json.decoder.JSONDecodeError:
                print('Щось не так з містом')

        elif choice == '2':
            city = input('Нове місто: ')

        elif choice == '0':
            break


main_menu()
