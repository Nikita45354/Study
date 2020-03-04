import random


list1 = random.sample(range(1, 999), 13)
list2 = [random.randint(1, 999) for _ in range(13)]

print('Два списка')
print(list1)
print(list2)

def max_ascendent_values_in_list(input_list: list):
    output_list = []
    for key, value in enumerate(input_list):
        if key+1 < len(input_list) and value < input_list[key+1]:
            output_list.append(input_list[key+1])

    return output_list

print('Результат общий:')
print(max_ascendent_values_in_list(list1))
print(max_ascendent_values_in_list(list2))
