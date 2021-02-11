def find_max_names(filename='marks.txt'):
    file = open(filename)
    max_mark = 0
    max_names = []
    for line in file:
        name, mark_str = line.split(' - ')
        mark = int(mark_str)
        if mark > max_mark:
            max_mark = mark
            max_names.clear()
            max_names.append(name)
        elif mark == max_mark:
            max_names.append(name)

    file.close()
    return max_names


print(find_max_names())
