spisok_stud = {'№': ['ФИО', 'Возраст', 'Группа'], '1': ['Иванов Иван Иванович', '30', 'БО-111111'],
               '2': ['Сидоров Семен Семенович', '30', 'БО-111111'], '3': ['Яшков Илья Петрович', '31', 'БО-222222'],
               '4': ['Андреев Алексей Викторович', '30', 'МИТ11']}
#1
def up_spisok(test_spisok):
    number = input('Введите номер студента: ')
    fio = input('Введите ФИО студента')
    age = input('Введите возраст студента: ')
    grup = input('Введите группу студента: ')
    new_stud = {number: [fio, age, grup]}
    test_spisok.update(new_stud)

#2
def change_fio(test_spisok):
    number = input('ФИО какого студента хотите изменить: ')
    test_spisok[number][0] = input('Введите новое ФИО')

def change_age(test_spisok):
    number = input('Возраст какого студента хотите изменить: ')
    test_spisok[number][1] = input('Введите новый возраст')

def change_grup(test_spisok):
    number = input('Номер группы какого студента хотите изменить: ')
    test_spisok[number][2] = input('Введите новый номер')

def change_complex(test_spisok):
    print('Если хотите изменить все данные студента введите "vse"')
    print('Если хотите изменить ФИО - "fio"')
    print('Если хотите изменить возраст - "age"')
    print('Если хотите изменить номер группы - "grup"')
    vibor = input('Какие данные хотите изменить: ')
    if vibor == 'fio':
        change_fio(test_spisok)
    elif vibor == 'age':
        change_age(test_spisok)
    elif vibor == 'grup':
        change_grup(test_spisok)
    elif vibor == 'vse':
        number = input('Данные какого студента хотите изменить: ')
        test_spisok[number][0] = input('Введите новое Фио: ')
        test_spisok[number][1] = input("Введите новый возраст: ")
        test_spisok[number][2] = input('Введите новую группу')


#3
def delit_eliment(test_spisok):
    number = input("Enter a number: ")
    del test_spisok[number]

#4
def show_stud(test_spisok):
    number = input('Enter a number')
    print(test_spisok[number][0])
    print(test_spisok[number][1])
    print(test_spisok[number][2])