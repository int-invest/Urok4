from itertools import count, cycle

for i in count(4):
    if i > 20:
        break
    else:
        print(i)


'''Задание Б'''
my_list = [103, 'abcsm', True, 4, 'DFk']
i = 0
for a in cycle(my_list):
    if i > 10:
        break
    print(a)
    i += 1