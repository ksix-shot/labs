import csv


def kaf_and_doljn(way):
    arr2 = []
    with open(way, encoding='utf-8', newline="") as file:

        reader = csv.reader(file)

        for row in reader:
            cur_arr = row[0].split(';')
            arr2.extend([cur_arr])
    for x in arr2:
        global kafedr, doljn
        if x[3] not in kafedr:
            kafedr.append(x[3])
        if x[4] not in doljn:
            doljn.append(x[4])


def spiski(way):
    global doljn, kafedr
    test_dict = {}
    arr2 = []
    with open(way, encoding='utf-8', newline="") as file:

        reader = csv.reader(file)

        for row in reader:
            cur_arr = row[0].split(';')
            arr2.extend([cur_arr])
    for x in arr2:
        doljn_prepod = 0
        kafedra = 0
        while True:
            for y in range(len(kafedr)):
                if kafedr[y] == x[3]:
                    kafedra = y
                    break
            for y in range(len(doljn)):
                if doljn[y] == x[4]:
                    doljn_prepod = y
                    break
            break
        x = {x[0]: [x[1], x[2], kafedra, doljn_prepod]}
        test_dict.update(x)
    return test_dict


doljn = []
kafedr = []
spisok_prepod = spiski('ex2.csv')


def spisok_kafedr():
    global kafedr
    print('Кафедры:')
    for x in range(len(kafedr)):
        print(f'{x + 1} {kafedr[x]}')


def spisok_doljn():
    global doljn
    print("Должности")
    for x in range(len(doljn)):
        print(f'{x + 1} {doljn[x]}')


def izmen_doljn():
    spisok_doljn()
    vibor = int(input('Какой элемент хотите изменить, укажите номер позиции: '))
    print(f'Введите новое название для "{doljn[vibor]}"')
    zamena = input('>')
    doljn[vibor] = zamena

def izmen_kaf():
    spisok_doljn()
    vibor = int(input('Какой элемент хотите изменить, укажите номер позиции: '))
    print(f'Введите новое название для "{kafedr[vibor]}"')
    zamena = input('>')
    kafedr[vibor] = zamena

def dobav(listik):
    print("Введите название нового элемента списка")
    listik.append(input('>'))


def dobav_prepodov():
    global spisok_prepod
    name = input('Введите ФИО')
    age = input("Введите возраст")
    spisok_kafedr()
    kaf = int(input('Выбирете кафедру:\n>'))
    spisok_doljn()
    dol = int(input("Выберете должность: \n>"))
    number = str(max(spisok_prepod.keys()) + 1)  ##Молюсь
    x = {number: [name, age, (kaf - 1), (dol - 1)]}
    spisok_prepod.update(x)


def spisok_prepodov():
    print('BASE')
    for i, y in spisok_prepod.items():
        print(f'{i}-- {y[0]} {y[1]} {kafedr[y[2]]} {doljn[y[3]]}')


def izmenenie_dan_prepod():
    global spisok_prepod
    print('Введите номер преподователя: ')
    prepod = input('> ')
    smena = input('Что хотите поменять (1 - Должность, 2 - Кафедра, 3 - Возраст')
    if smena == '1':
        spisok_doljn()
        vibor_dolj = input('Введите номер новой должности: ')
        spisok_prepod[prepod][3] = int(vibor_dolj)
    elif smena == '2':
        spisok_kafedr()
        vibor_dolj = input('Введите номер новой кафедры: ')
        spisok_prepod[prepod][4] = int(vibor_dolj)
    elif smena == '3':
        vozr = input('Введите возраст: ')
        spisok_prepod[prepod][1] = vozr


def csv_writer(data, path):
    for i in data.key:
        data[i][2] = kafedr[data[i][2]]
        data[i][3] = doljn[data[i][3]]

    with open(path, "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for key, value in data.items():
            i = [key, value]
            writer.writerow(i)


while True:
    what_doing = input('''Выбирете действие:
    1 - Преподователи
    2 - Должности
    3 - Кафедры
    4 - выйти из программы''')
    if what_doing == '1':
        what_doing_razdel = input('''Выбирете действие:
        1 - Измение преподователя
        2 - добавление нового
        3 - Просмотр списка
        4 - назад''')
        if what_doing_razdel == '1':
            izmenenie_dan_prepod()
        elif what_doing_razdel == '2':
            dobav_prepodov()
        elif what_doing_razdel == '3':
            spisok_prepodov()

    elif what_doing == '2':
        what_doing_razdel = input('''Выбирете действие:
                1 - Измение должности
                2 - добавление новой
                3 - Просмотр списка
                4 - назад''')
        if what_doing_razdel == '1':
            izmen_doljn()
        elif what_doing_razdel == '2':
            dobav(doljn)
        elif what_doing_razdel == '3':
            spisok_doljn()

