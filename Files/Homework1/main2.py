def writer(txt1, txt2):
    file = open(txt1, 'rt')

    names = file.read().split()
    file.close()

    file = open(txt2, 'wt')

    # i = len(names) - 1
    # while i >= 0:
    #     file.write(names[i] + ' ')
    #     i -= 1

    names.reverse()
    for name in names:
        file.write(name + ' ')

    file.close()


writer('see.txt', 'write.txt')
