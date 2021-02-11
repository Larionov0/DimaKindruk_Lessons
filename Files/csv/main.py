from json import dumps


def get_kidnappers(filename='kidnappers.csv'):
    """
    :param filename: str
    :return: [{},{},{},{}]    (список із словників-викрадачів)
    """
    kidnappers_list = []
    file = open(filename, 'rt', encoding='utf-8')
    headers = file.readline()
    for line in file:
        line_list = line.rstrip().split(', ')  # ['Боб', 'Булька', 'Бобові', '27', 'літаюча тарілка; засмоктувач; люлька']
        kidnapper_dict = {
            'ім`я': line_list[0],
            'планета': line_list[1],
            'раса': line_list[2],
            'викрадення': int(line_list[3]),
            'девайси': line_list[4].split('; ')
        }
        kidnappers_list.append(kidnapper_dict)
    return kidnappers_list


def find_best_rasa():
    kidnappers = get_kidnappers()

    rasa_count_dict = {}

    for kidnapper_dict in kidnappers:
        rasa = kidnapper_dict['раса']
        count = kidnapper_dict['викрадення']

        if rasa not in rasa_count_dict:
            rasa_count_dict[rasa] = 0
        rasa_count_dict[rasa] += count

    max_ = 0
    max_rasa = ''
    for rasa in rasa_count_dict:
        if rasa_count_dict[rasa] > max_:
            max_ = rasa_count_dict[rasa]
            max_rasa = rasa

    return max_rasa


print(find_best_rasa())
