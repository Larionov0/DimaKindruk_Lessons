def get_average_age(students):
    age_sum = 0
    count = 0
    for group_name in students:
        group = students[group_name]
        for student in group:
            age_sum += student['age']
            count += 1

    return age_sum / count


def find_names_of_all_students_that_loves_hobby(students, hobby):
    for group_name in students:  # 'A'
        group = students[group_name]  # [{}, {}, {}]
        for student in group:
            if hobby in student['hobbies']:
                print(student['name'])


def best_group_by_subject(students, subject):
    max_mark = 0
    groups_with_max_mark = []
    for group_name in students:
        group = students[group_name]
        total_sum = 0
        count = 0
        for student in group:
            mark = student['marks'][subject]
            total_sum += mark
            count += 1

        average_mark = total_sum / count
        if average_mark > max_mark:
            max_mark = average_mark
            groups_with_max_mark.clear()
            groups_with_max_mark.append(group_name)
        elif average_mark == max_mark:
            groups_with_max_mark.append(group_name)

    return groups_with_max_mark


students = {
    'A': [
        {
            'name': 'Vasya',
            'email': 'vasyok228@',
            'age': 12,
            'hobbies': ['games', 'eat'],
            'marks': {
                'Python': 8,
                'math': 6,
                'English': 8
            }
        },
        {
            'name': 'Masha',
            'email': 'mashok228@',
            'age': 15,
            'hobbies': ['books', 'eat'],
            'marks': {
                'Python': 9,
                'math': 10,
                'English': 12
            }
        },
        {
            'name': 'Bob',
            'email': 'bob4ik@',
            'age': 14,
            'hobbies': ['sport', 'fishing'],
            'marks': {
                'Python': 7,
                'math': 6,
                'English': 5
            }
        },
    ],
    'B': [
        {
            'name': 'Petro',
            'email': 'peet@',
            'age': 15,
            'hobbies': ['books', 'swimming', 'programming'],
            'marks': {
                'Python': 12,
                'math': 10,
                'English': 10
            }
        },
        {
            'name': 'Dima',
            'email': 'dimas@',
            'age': 13,
            'hobbies': ['games', 'montage'],
            'marks': {
                'Python': 9,
                'math': 10,
                'English': 8
            }
        },
    ],
    "C": [
        {
            'name': 'Sasha',
            'email': 'larko@',
            'age': 16,
            'hobbies': ['programming', 'eat', 'games', 'football'],
            'marks': {
                'Python': 12,
                'math': 9,
                'English': 8
            }
        },
        {
            'name': 'Ira',
            'email': 'irinka@',
            'age': 13,
            'hobbies': ['math', 'books', 'cartoons'],
            'marks': {
                'Python': 10,
                'math': 11,
                'English': 12
            }
        },
    ]
}


print(best_group_by_subject(students, 'math'))
