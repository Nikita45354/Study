my_list = [True, 'ABCD', 12223, None]

print('_____________')
for el in cycle(my_list):
    cnt +=1
    print(el)
    if cnt >= limit:
        cnt = 0
        break
