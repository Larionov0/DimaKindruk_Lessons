from os import system
import random

n = 12
m = 16

# Create matrix
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

# Создание персонажа
hero_face = '#'
hero_coords = [5, 5]
hero_hp = 6
hero_details = 0

animals = [
    # [type, name, hp, face, coords]
    ['kurka', 'Ryaba', 3, 'k', [1, 1]],
    ['kurka', 'Tupka', 3, 'k', [1, 2]],
    ['kurka', 'Abuba', 3, 'k', [2, 1]]
]

hod = 0
while True:
    system('cls')
    # Поместить персонажа на поле
    matrix[hero_coords[0]][hero_coords[1]] = hero_face

    # Помещаем куриц на поле
    for animal in animals:
        animal_coords = animal[4]
        animal_face = animal[3]
        matrix[animal_coords[0]][animal_coords[1]] = animal_face

    # Print matrix
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

    matrix[hero_coords[0]][hero_coords[1]] = '-'

    for animal in animals:
        animal_coords = animal[4]
        animal_face = animal[3]
        matrix[animal_coords[0]][animal_coords[1]] = '-'

    # Персонаж ходить
    print(f"Details: {hero_details}")
    choice = input("WASD\n")

    if choice == 'w':
        if hero_coords[0] != 0:
            hero_coords[0] -= 1
    elif choice == 'a':
        if hero_coords[1] == 0:
            hero_coords[1] = m - 1
        else:
            hero_coords[1] -= 1
    elif choice == 's':
        if hero_coords[0] != n - 1:
            hero_coords[0] += 1
    elif choice == 'd':
        if hero_coords[1] == m - 1:
            hero_coords[1] = 0
        else:
            hero_coords[1] += 1

    # Поймал ли курку
    for animal in animals:
        if animal[0] == 'kurka':
            if animal[4] == hero_coords:
                animals.remove(animal)
                hero_details += 3

    # Курка ходит
    for animal in animals:
        animal_coords = animal[4]
        side = random.choice(['w', 'a', 's', 'd'])
        if side == 'w':
            if animal_coords[0] != 0:
                animal_coords[0] -= 1
        elif side == 'a':
            if animal_coords[1] == 0:
                animal_coords[1] = m - 1
            else:
                animal_coords[1] -= 1
        elif side == 's':
            if animal_coords[0] != n - 1:
                animal_coords[0] += 1
        elif side == 'd':
            if animal_coords[1] == m - 1:
                animal_coords[1] = 0
            else:
                animal_coords[1] += 1

    # Поймал ли курку
    for animal in animals:
        if animal[0] == 'kurka':
            if animal[4] == hero_coords:
                animals.remove(animal)
                hero_details += 3

    # Спавн курки
    if hod % 20 == 0:
        kurka = ['kurka', 'New', 3, 'k', [random.randint(0, n - 1), random.randint(0, m - 1)]]
        animals.append(kurka)
    hod += 1
