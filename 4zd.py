import random

pos1 = int(input("Введите позицию 1: "))
pos2 = int(input("Введите позицию 2: "))
n = int(input("Введите число N: "))

my_list = []
for i in range(-n, n+1):
    my_list.append(random.randint(-n,n))
print(my_list)
print(" ")

f = 1
for el in my_list[pos1:pos2 + 1]:
    f *= el
print(f)
