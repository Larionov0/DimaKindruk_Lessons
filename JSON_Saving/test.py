from msvcrt import getch


def press(message):
    print(message)
    sym = getch()
    return str(sym)[2:-1]


print(press('Kek: '))
