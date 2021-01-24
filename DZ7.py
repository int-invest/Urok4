from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)


func = fact()

try:
    a = 0
    n = int(input("Ведите число: "))
    for i in func:
        if a < n:
            print(i)
            a += 1
        else:
            break
except ValueError:
    print("Вы ввели не число!!!")

