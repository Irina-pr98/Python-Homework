# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

number = int(input('Введитее число: '))
degree = int(input('Введитее степень: '))

def function(number, degree):
    if degree == 0:
        return 1
    return number * function(number, degree -1)
print(f'{number} в степени {degree} = {function(number, degree)}')