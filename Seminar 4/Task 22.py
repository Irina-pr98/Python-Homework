"""
Даны два неупорядоченных набора целых чисел (может быть, 
с повторениями). Выдать без повторений в порядке возрастания все те 
числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""

import random
length_list_1 = int(input('Введите количество элементов первого списка: '))
length_list_2 = int(input('Введите количество элементов второго списка: '))

list_1 = [random.randint(1, 21) for _ in range(length_list_1)]
list_2 = [random.randint(1, 21) for _ in range(length_list_2)]

print(f'Первый список: {list_1}')
print(f'Второй список: {list_2}')
print(f'Итоговый список: {sorted(set(list_1).intersection(set(list_2)))}')