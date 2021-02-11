def helloer(name):
    print(f"Hello {name}!!!")


def love(name1, name2):
    print(f"{name1} loves {name2}")


def skleivatel(string1, string2):
    result = string1 + " = " + string2
    return result


def calcul(num1, oper, num2=None):
    if oper in ["+", "summ", "summa", "сума", "додати"]:
        return num1 + num2
    elif oper in ['-', 'minus', 'відняти', "решта"]:
        return num1 - num2
    elif oper in ['*', "mult", 'помножити', "добуток", 'на']:
        return num1 * num2
    elif oper in ['/', 'div', 'ділення', "поділити", "ділити"]:
        return num1 / num2
    elif oper in ["^", "до степеня", "степінь"]:
        return num1 ** num2
    elif oper in ["!", 'factorial', 'факторіал']:
        # 5! = 5 * 4 * 3 * 2 * 1
        result = 1
        number = 1
        while number <= num1:
            result = number * result
            number += 1

        return result


def find_max(lst):
    max_ = 0
    for number in lst:
        if max_ < number:
            max_ = number
    return max_


def count_of_letters(string, letter_input):
    point = 0
    for letter in string:
        if letter == letter_input:
            point += 1
    return point


c = count_of_letters("kek lol", 'h')
print(c)
