students = {
    "A": {
        'b0b4ik@gmail.com': {
            'name': 'Bob',
            'age': 12,
            'hobbies': ['Python', 'fishing', 'books'],
            'marks': {
                'Python': 9,
                'math': 9,
                'physic': 4,
                'English': 6
            }
        },
        'alenka@gmail.com': {
            'name': 'Alena',
            'age': 14,
            'hobbies': ['eat', 'games'],
            'marks': {
                'Python': 7,
                'math': 4,
                'physic': 3,
                'English': 7
            }
        },
        'M0sh1k@gmail.com': {
            'name': 'Misha',
            'age': 11,
            'hobbies': ['math', 'physic', 'books'],
            'marks': {
                'Python': 7,
                'math': 9,
                'physic': 9,
                'English': 8
            }
        }
    },
    "B": {
        'botan4ik@gmail.com': {
            'name': 'Bogdan',
            'age': 12,
            'hobbies': ['eat', 'games', 'football', 'sport'],
            'marks': {
                'Python': 2,
                'math': 1,
                'physic': 3,
                'English': 5
            }
        },
        'alan@gmail.com': {
            'name': 'Alan',
            'age': 12,
            'hobbies': ['football', 'hockey', 'bike'],
            'marks': {
                'Python': 7,
                'math': 8,
                'physic': 9,
                'English': 6
            }
        },
        'dasha@gmail.com': {
            'name': 'Dasha',
            'age': 10,
            'hobbies': ['eat', 'games', 'climbing', 'books'],
            'marks': {
                'Python': 9,
                'math': 10,
                'physic': 8,
                'English': 7
            }
        },
    },
    "C": {
        'vanya@gmail.com': {
            'name': 'Vanya',
            'age': 14,
            'hobbies': ['eat', 'coffee'],
            'marks': {
                'Python': 9,
                'math': 2,
                'physic': 1,
                'English': 2
            }
        },
        'yarik@gmail.com': {
            'name': 'Yaroslav',
            'age': 11,
            'hobbies': ['sleep', 'games'],
            'marks': {
                'Python': 10,
                'math': 7,
                'physic': 5,
                'English': 6
            }
        },
    }
}


def makrschildren (dikt):
    markall = 0
    marknum = 0

    for group_name in students:
        group = students[group_name]
        for mail in group:
            student = group[mail]
            markall += student['marks']['math']
            marknum += 1
    rezult = markall / marknum
    return rezult


a = makrschildren(students)
print(a)
