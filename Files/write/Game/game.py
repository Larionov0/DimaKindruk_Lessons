from json import dumps


def main_menu(enemies):
    while True:
        save(enemies)
        print("--= Головне меню =--")
        print('1 - додати ворога')
        print('2 - додати героя')
        print('3 - подивитися список')
        print('4 -  вийти')

        choice = input("Ваш вибір: ")
        if choice == '1':
            add_enemy(enemies)
        elif choice == '2':
            print("Coming soon...")
        elif choice == '3':
            watch_list(enemies)
        elif choice == '4':
            save(enemies)
            break


def add_enemy(enemies):
    name = input('Імя: ')
    attack = int(input('Атака: '))
    hp = int(input('HP: '))
    armor = int(input('Armor: '))
    loot = input_list('Введіть лут:')
    enemies.append({
        'name': name,
        'attack': attack,
        'hp': hp,
        'armor': armor,
        'loot': loot
    })


def input_list(string):
    lst = []
    while True:
        print(string)
        item = input()
        if item == 'stop':
            break
        else:
            lst.append(item)
    return lst


def watch_list(enemies):
    print(dumps(enemies, indent=4, ensure_ascii=False))


def save(enemies, filename='game_info.csv'):
    file = open(filename, 'wt', encoding='utf-8')
    file.write('name, attack, hp, armor, loot\n')
    for enemy in enemies:
        line = f'{enemy["name"]}, {enemy["attack"]}, {enemy["hp"]}, {enemy["armor"]}, {"; ".join(enemy["loot"])}\n'
        file.write(line)
    file.close()


def get_info_from_file(filename='game_info.csv'):
    file = open(filename, 'rt', encoding='utf-8')
    file.readline()
    enemies = []
    for line in file:
        enemy_list = line.rstrip().split(', ')
        enemy = {
            'name': enemy_list[0],
            'attack': int(enemy_list[1]),
            'hp': int(enemy_list[2]),
            'armor': int(enemy_list[3]),
            'loot': enemy_list[4].split('; ')
        }
        enemies.append(enemy)

    file.close()
    return enemies


enemies = get_info_from_file()
main_menu(enemies)
