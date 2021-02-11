from random import choices, choice
from json import loads
import random


class Human:
    names = None

    def __init__(self, sex, name, age=0, money=0):
        self.sex = sex  # "Ч"/"Ж"
        self.name = name
        self.age = age
        self.money = money
        # print('Нова людина народжена: ' + self.name)

    def say_hi(self):
        print(f"{self.name}: Привіт!")

    def say_hi_to_someone(self, other):
        print(f"{self.name}: Привіт, {other.name}")

    def grow_up(self):
        self.age += 1
        print(f"У {self.name} день народження! Йому тепер {self.age}")

    @classmethod
    def load_names_from_file(cls, filename='names.json'):
        with open(filename, 'rt', encoding='utf-8') as file:
            dct = loads(file.read())

        cls.names = dct

    @classmethod
    def get_names(cls):
        if cls.names is None:
            cls.load_names_from_file()
        return cls.names

    def __gt__(self, other):  # >  "greater than"
        # return len(self.name) > len(other.name)  - як варіант
        return self.age > other.age

    def __eq__(self, other):  # ==
        return self.name == other.name and self.age == other.age

    def __str__(self):  # str
        if self.sex == 'Ч':
            tpe = 'Чоловік'
            word = 'Йому'
        else:
            tpe = 'Жінка'
            word = 'Їй'
        return f"{tpe} {self.name}. {word} {self.age}"

    @classmethod
    def gen_name(cls, sex):
        names = Human.get_names()
        if sex == "Ч":
            names = names['Чоловічі']
        else:
            names = names['Жіночі']
        names_list = []
        freq_list = []
        for name in names:
            names_list.append(name)
            freq_list.append(names[name])
        name = choices(names_list, freq_list)[0]
        return name

    def __add__(self, other):  # +
        if self.age >= 16 and other.age >= 16:
            if self.sex != other.sex:
                sex = choice(["Ч", "Ж"])
                name = Human.gen_name(sex)

                baby = Human(sex, name)
                return baby

    def become_worker(self, job):
        new_worker = Worker(self.sex, self.name, job, self.age, self.money)
        return new_worker


class Worker(Human):
    def __init__(self, sex, name, job, age=0, money=0):
        super().__init__(sex, name, age, money)
        self.job = job

    def work(self):
        print(f"{self.name} працює...")
        self.money += 100

    def say_hi(self):
        print(f"{self.name}: Привіт від робочих")

    def grow_up(self):
        super().grow_up()
        premia = 100
        self.money += premia
        print(f"{self.name} отримав премію: {premia}")

    def __str__(self):
        return f"Робітник {super().__str__()}\n" \
               f"Робота: {self.job}"


class Gamer(Human):
    def __init__(self, sex, name, lovely_games=None, age=0, money=0):
        super().__init__(sex, name, age, money)
        if lovely_games is None:
            lovely_games = []
        self.lovely_games = lovely_games

    def play(self):
        game = random.choice(self.lovely_games)
        print(f"{self.name} грає в {game}")


class ProGamer(Gamer):
    def play(self):
        super().play()
        zar = random.randint(0, 400)
        self.money += zar
        print(f"{self.name} заробив {zar} $")


h1 = Human('Ч', 'Bob', 10)
h2 = Worker('Ч', 'Patrik', 'зварювальник', 25)
h3 = Worker('Ж', "Аліса", "програміст", 19)

h4 = Gamer("Ж", "Альона", ['CS GO', 'Starcraft'], 18)

h5 = ProGamer("М", "Льоша", ["LOL", 'Super Mario'], 2)

h5.play()
