import os

DIR = 'files'
file_path = os.path.join(DIR, 'task1.txt')
file = open(file_path, 'a',  encoding='utf-8')

while True:
    string = input('Поле ввода: ')

    if not string:
        file.close()
        print('Выход')
        break

    file.write(f'{string}\n')
