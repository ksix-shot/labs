mat = [[1, 2, 3, 4, 5, 6, 7, 8],
       [8, 7, 6, 5, 4, 3, 2, 1],
       [2, 3, 4, 5, 6, 7, 8, 9],
       [9, 8, 7, 6, 5, 4, 3, 2],
       [1, 3, 5, 7, 9, 7, 5, 3],
       [3, 1, 5, 3, 2, 6, 5, 7],
       [1, 7, 5, 9, 7, 3, 1, 5],
       [2, 6, 3, 5, 1, 7, 3, 2]]


def zad_1(listik):
    for i in range(len(listik)):
        for x in range(len(listik[i])):
            listik[i][x] = listik[i][x] ** 2


def zad_2(listik):
    for i in range(len(listik)):
        for x in range(len(listik[i])):
            if listik[i][x] % 2 == 0:
                listik[i][x] = listik[i][x] ** 2


def zad_3(listik):
    for i in range(len(listik)):
        for x in range(len(listik[i])):
            if listik[i][x] < 5:
                listik[i][x] = listik[i][x] ** 2


def zad_4(listik):
    for i in range(4):
        for x in range(len(listik[i])):
            listik[i][x] = listik[i][x] ** 2
