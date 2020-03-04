import os

DIR = 'files'
file_to_read_path = os.path.join(DIR, 'task4.txt')
file_to_write_path = os.path.join(DIR, 'task4-cyr.txt')

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()

with open(file_to_write_path, 'a', encoding='utf-8') as file_write:
    for line in lines:
        row = line.split()
        row[0] = dictionary[row[0]]
        print(' '.join(row), file=file_write)
