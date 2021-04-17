#First
import operator
import csv
d = {'dict': 1, 'dictionary': 2}
print(len(d.keys()))

filepath = "./ex1.csv"
arr2 = []
with open(filepath, encoding='utf-8', newline="") as file:
    #читаем файл целиком
    reader = csv.reader(file)
    '''
    Циклом for проходим по строкам 
    '''
    for row in reader:
        cur_arr = row[0].split(';')
        arr2.extend([cur_arr])
test_dict = {}
for x in arr2:
    x = {x[0]: [x[1], x[2], x[3]]}
    test_dict.update(x)


def print_list(test_dict):
    b = sorted(test_dict.items(), key = operator.itemgetter(1))
    for x,y in b:
        if x != '№':
            print(str(x)+', '+y[0] + ', возраст: ' + y[1]+', №: ' + y[2])


def up_age(test_dicts):
    for x, y in test_dicts.items():
        if x != '№':
            y[1] = int(y[1])
            y[1] += 1
            y[1] = str(y[1])


def csv_writer(data, path):

    """
    Функция для записи данных в CSV
    """
    with open(path, "w", newline='', encoding='utf-8') as csv_file:
        '''
        csv_file - объект с данными
        delimiter - разделитель
        '''
        writer = csv.writer(csv_file, delimiter=';')
        for key, value in data.items():
            i = [key, value]
            writer.writerow(i)




