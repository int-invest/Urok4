from functools import reduce

def my_func():
    new_list = [i for i in range(99, 1001) if i % 2 == 0]
    sum_all = reduce(lambda x,y: x * y, new_list)
    return sum_all

print(my_func())


