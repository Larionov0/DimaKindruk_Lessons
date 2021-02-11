def get_names_from_file(filename='info.txt'):
    names = []
    file = open('info.txt', 'rt', encoding='utf-8')

    for line in file:  # line = "Одесса, Гаків, Миколаїв, Ффпвра\n"
        line_words = line.rstrip().split(',')

        for word in line_words:
            names.append(word.strip())

    file.close()
    return names


print(get_names_from_file())
