import os

DIR = 'files'
file_path = os.path.join(DIR, 'task3.txt')
file = open(file_path, 'r', encoding='utf-8')
lines = file.readlines()

sum = 0
for row in lines:
    line = row.split()

    if (float(line[1]) < 20000):
        print(f'{line[0]} Имеет оклад менее 200руб')

    sum += float(line[1])

print(f'В среднем вот такой зароботок: {sum} руб')

file.close()
