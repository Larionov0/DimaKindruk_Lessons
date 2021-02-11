def get_max_money(clients):
    max_money = 0
    max_surname = ''
    for client in clients:
        if client['money'] > max_money:
            max_surname = client['surname']
            max_money = client['money']

    print(max_surname)
    print(max_money)


def get_age_money_corelation(clients):
    """
    молодий: 0 - 20 років
    середній: 21 - 40 років
    похилий: 41 - 150 років

    :param clients: {}
    :return:
    {
        "молоді": 11500,
        "середні": 50000,
        "похилі": 1000
    }
    """
    molod = {
        'сума': 0,
        'кількість': 0
    }
    sered = {
        'сума': 0,
        'кількість': 0
    }
    pohyl = {
        'сума': 0,
        'кількість': 0
    }

    for client in clients:
        if client['age'] <= 20:
            molod['кількість'] += 1
            molod['сума'] += client['money']

        elif 21 <= client['age'] <= 40:
            sered['кількість'] += 1
            sered['сума'] += client['money']

        elif 41 <= client['age']:
            pohyl['кількість'] += 1
            pohyl['сума'] += client['money']

    return {
        "молоді": molod['сума'] / molod['кількість'],
        "середні": sered['сума'] / sered['кількість'],
        "похилі": pohyl['сума'] / pohyl['кількість']
    }


clients = [
    {
        'surname': 'Bobchenko',
        'age': 20,
        'money': 1400
    },
    {
        'surname': 'Makarenko',
        'age': 42,
        'money': 16000
    },
    {
        'surname': 'Totti',
        'age': 32,
        'money': 9500
    },
    {
        'surname': 'Abubiy',
        'age': 39,
        'money': 145000
    },
    {
        'surname': 'Puzyrchenko',
        'age': 18,
        'money': 10400
    },
    {
        'surname': 'Ioio',
        'age': 16,
        'money': 500
    },
    {
        'surname': 'Ruster',
        'age': 67,
        'money': 52000
    },
    {
        'surname': 'Alankova',
        'age': 28,
        'money': 34400
    },
    {
        'surname': 'Vupsen',
        'age': 52,
        'money': 5200
    },
    {
        'surname': 'Gogo',
        'age': 32,
        'money': 32100
    },
    {
        'surname': 'Dupsen',
        'age': 17,
        'money': 4000
    },
    {
        'surname': 'Patrik',
        'age': 61,
        'money': 6000
    },
]


print(get_age_money_corelation(clients))
