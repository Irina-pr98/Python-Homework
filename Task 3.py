# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме 
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

number = input('Введите шестизначный номер билета: ')
first_three_digits = int(number[0]) + int(number[1]) + int(number[2])
last_three_digits = int(number[3]) + int(number[4]) + int(number[5])
print(f'Сумма первых трех цифр равна: {first_three_digits}')
print(f'Сумма последних трех цифр равна: {last_three_digits}')
if first_three_digits == last_three_digits:
    print('yes')
else:
    print('no')