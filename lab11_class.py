import csv


class Grup:
    def __init__(self, nazvan):
        self.nazvan = nazvan
        self.spisok = []
    def __str__(self):
        return self.nazvan

    def izmen(self, new_nazv):
        self.nazvan = new_nazv


class Prepod:
    def __init__(self, fio, age, grup='', doljn=''):
        self.fio = fio
        self.age = age
        self.grup = grup
        self.doljn = doljn

    def __str__(self):
        return 'Name ' + self.fio + '\nGrup ' + self.grup + '\nPosition ' + self.doljn


class Doljn:
    def __init__(self, nazv):
        self.nazv = nazv

    def __str__(self):
        return self.nazv

    def izm_doljn(self, new_name):
        self.nazv = new_name

def show_all_prepod(listik):
    for x in listik:
        print('*********')
        print(x)


def modul_cvs(way):
    test_dict = {}
    arr2 = []
    with open(way, encoding='utf-8', newline="") as file:

        reader = csv.reader(file)

        for row in reader:
            cur_arr = row[0].split(';')
            arr2.extend([cur_arr])
    for x in arr2:
        x = {x[0]: [x[1], x[2], x[3]]}
        test_dict.update(x)
    return test_dict

#def create_class(slov):
    #for name, val, number in slov.items, range(len(slov.key())):

a = Prepod('Иван', 6)
print(a)