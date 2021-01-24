my_list = [1, 50, 2, 3, 4, 1, 5, 7, 3, 6, 10, 14, 4]
new_list =[i for i in my_list if my_list.count(i) < 2]
print(new_list)
