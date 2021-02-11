def get_element(lst, i):
    num = lst[i]
    return num


def isdigit(string):
    """
    string:  "13451";  "12e3rf24";  "12r1123"
    """
    result = True
    for symbol in string:
        if symbol not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result = False
    return result


def input_number(message, error_message="Не число. Спробуйте ще раз."):
    while True:
        ans = input(message)
        if isdigit(ans):
            return int(ans)
        else:
            print(error_message)


def lol(n):
    """
    n = 4
    return [4, 4, 4, 4]

    n = 6
    return [6, 6, 6, 6, 6, 6]
    """
    lst = []
    i = 0
    while i != n:
        lst.append(n)
        i += 1
    return lst


i = 0
for el in lol(100000):
    print(i, el)
    i += 1
