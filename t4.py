source_list = [1, 1, 2, 2, 33, 44, 3, 22, 12, 2, 32, 22, 33, 44]
my_new_list = [i for i in source_list if source_list.count(i) < 2]
print(my_new_list)
