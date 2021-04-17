
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


def up_age(spisok_stud):
    fio = input('Введите ФИО студента, которому желаете увеличить возраст: ')
    for i in spisok_stud.keys():
        if fio in spisok_stud[i]:
            spisok_stud[i][1] = str(int(spisok_stud[i][1]) + 1)

def show_po_grup(spisok_stud):
    grup = input('Введите искомую группу: ')
    for i in spisok_stud.keys():
        if grup in spisok_stud[i]:
            print('№' + i)
            print('ФИО'+ spisok_stud[i][0])
            print("Группа номер: " + spisok_stud[i][2])


print(test_dict)
show_po_grup(test_dict)