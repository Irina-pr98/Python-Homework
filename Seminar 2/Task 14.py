# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

num = int(input('Введите число: '))
prod = 0
degree = 0
while prod * 2 < num:
    prod = 2 ** degree
    print(prod, end=' ')
    degree += 1