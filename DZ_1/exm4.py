#Напишите программу, которая по заданному номеру четверти, показывает диапазон 
#возможных координат точек в этой четверти (x и y).

d = int(input('Введите номер четверти: '))
if d < 1 or d > 4:
     print('введите корректно')
elif d == 1:
     print('x > 0 и y > 0')
elif d == 2:
     print('x < 0 и y > 0')
elif d == 3:
     print('x < 0 и y < 0')
elif d == 4:
     print('x > 0 и y < 0')