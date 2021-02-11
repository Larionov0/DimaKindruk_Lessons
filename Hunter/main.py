import random
from os import system
from msvcrt import getch
from time import sleep

n = 14
m = 16


def press(message):
    print(message)
    klava = getch()  # b'a'
    return chr(ord(klava))


def clear():
    system('cls')


def create_matrix(n, m):
    matrix = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < m:
            row.append('-')
            j += 1
        matrix.append(row)
        i += 1
    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        text = "|"
        j = 0
        while j < len(matrix[i]):
            text += str(matrix[i][j]) + " "
            j += 1
        text = text[:-1] + "|"
        print(text)
        i += 1


def print_pole(pole):
    clear()
    print_matrix(pole)


def player_make_hod(pole, hero):
    print("--= Меню дій =--")
    print(f"Ваші деталі: {hero['details']}")
    print('WASD - переміщення')

    choice = press('Ваш вибір: ')
    if choice in ['w', 'a', 's', 'd']:
        creature_moves_1(hero, choice)

    elif choice == 'x':
        hero_shoots(hero, animals, pole)


def hero_shoots(hero, animals, pole):
    if hero['weapon']['type'] == 'bow':
        bow_shoots(hero, animals, pole)
    elif hero['weapon']['type'] == 'slingshot':
        pass


def bow_shoots(hero, animals, pole):
    clear()
    place_creatures(animals, pole)
    place_creature(hero, pole)
    print_pole(pole)
    clear_creatures_from_pole(animals, pole)
    clear_creature_from_pole(hero, pole)
    dir = press("WASD - вибери напрям вистрілу: ").lower()

    if dir in ['w', 'a', 's', 'd']:
        arrow = {
            'type': 'arrow',
            'damage': hero['weapon']['damage'],
            'energy': hero['weapon']['range'],
            'coords': hero['coords'].copy(),
            'face': '+',
            'direction': dir
        }
        arrow_flying(arrow, animals, pole, hero)


def arrow_flying(arrow, animals, pole, hero):
    while arrow['energy'] >= 0:
        clear()
        place_creatures(animals, pole)
        place_creature(hero, pole)
        place_creature(arrow, pole)
        print_pole(pole)
        clear_creature_from_pole(arrow, pole)
        clear_creatures_from_pole(animals, pole)
        result = check_collision(arrow, animals, hero)
        if result:
            return
        creature_moves_1(arrow, arrow['direction'])
        arrow['energy'] -= 1
        sleep(0.1)


def check_collision(arrow, animals, hero):
    for animal in animals:
        if arrow['coords'] == animal['coords']:
            animal_got_damage(animal, arrow['damage'], hero)
            return True
    return False


def animal_got_damage(animal, damage, hero):
    animal['hp'] -= damage
    if animal['hp'] <= 0:
        animal_die(animal, animals, hero)


def kurka_make_hod(kurka):
    direction = random.choice(['w', 'a', 's', 'd'])
    creature_moves_1(kurka, direction)


def animal_make_hod(animal):
    if animal['type'] == 'kurka':
        kurka_make_hod(animal)
    elif animal['type'] == 'pig':
        pass


def animals_make_hod(animals):
    for animal in animals:
        animal_make_hod(animal)


def creature_moves_1(creature, direction):
    if direction == 'w':
        if creature['coords'][0] != 0:
            creature['coords'][0] -= 1
    elif direction == 'a':
        if creature['coords'][1] == 0:
            creature['coords'][1] = m - 1
        else:
            creature['coords'][1] -= 1
    elif direction == 's':
        if creature['coords'][0] != n - 1:
            creature['coords'][0] += 1
    elif direction == 'd':
        if creature['coords'][1] == m - 1:
            creature['coords'][1] = 0
        else:
            creature['coords'][1] += 1


def place_creature(creature, pole):
    coords = creature['coords']
    pole[coords[0]][coords[1]] = creature['face']


def place_creatures(creatures, pole):
    """
    Функція для того щоб покласти кожне створіння із списка на поле
    :param creatures: list   (список створінь (animals / players))
    :param pole: list (матриця)
    """
    for creature in creatures:
        place_creature(creature, pole)


def clear_creature_from_pole(creature, pole):
    coords = creature['coords']
    pole[coords[0]][coords[1]] = '-'


def clear_creatures_from_pole(creatures, pole):
    for creature in creatures:
        clear_creature_from_pole(creature, pole)


def ne_poimal_li_kurku(hero, animals):
    for animal in animals:
        if animal['type'] == 'kurka':
            if animal['coords'] == hero['coords']:
                animal_die(animal, animals, hero)


def animal_die(animal, animals, hero):
    rewards = {
        'kurka': 3,
        'pig': 8
    }

    animals.remove(animal)
    hero['details'] += rewards[animal['type']]


hero = {
    'name': 'Bob',
    'coords': [4, 4],
    'face': '#',
    'details': 0,
    'hp': 10,
    'max_hp': 10,
    'weapon': {
        'type': 'bow',
        'name': 'base Bow',
        'damage': 3,
        'range': 3,
        'details': 30,
        'description': 'зброя нуба'
    }
}

animals = [
    {
        'type': 'kurka',
        'name': 'Ryaba',
        'hp': 3,
        'face': 'k',
        'coords': [1, 1]
    },
    {
        'type': 'kurka',
        'name': 'Masha',
        'hp': 3,
        'face': 'k',
        'coords': [1, 2]
    },
    {
        'type': 'kurka',
        'name': 'Natasha',
        'hp': 3,
        'face': 'k',
        'coords': [2, 1]
    },
]

pole = create_matrix(n, m)

while True:
    place_creature(hero, pole)
    place_creatures(animals, pole)
    print_pole(pole)
    clear_creature_from_pole(hero, pole)
    clear_creatures_from_pole(animals, pole)
    player_make_hod(pole, hero)
    ne_poimal_li_kurku(hero, animals)
    animals_make_hod(animals)
    ne_poimal_li_kurku(hero, animals)
