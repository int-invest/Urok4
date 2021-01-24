
my_list = [1, 10, 12, 9, 13, 14, 5, 2, 5, 5, 10]
new_list = [i for a, i in enumerate(my_list) if my_list[a-1] < my_list[a]]
print(new_list)
