def filterer(numbers):
    numbers10 = []
    for number in numbers:
        if number > 10:
            numbers10.append(number)
    return numbers10


def create_dict(lst1, lst2):
    dct = {}
    i = 0
    while i < len(lst1):
        key = lst1[i]
        value = lst2[i]

        dct[key] = value
        i += 1

    return dct


def numberu20(numbers, num):
    numbers2 = []
    for number in numbers:
        if number > num:
            numbers2.append(number)
    return min(numbers2)


numbers = [1, 23, 4, 56, 12, 15, 3, 5, 7, 19]
num = 10
print(numberu20(numbers, num))
