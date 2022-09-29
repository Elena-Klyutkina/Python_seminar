# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def number(numb_a, numb_b):
    array_numb_a = [int(x) for x in numb_a.split()]
    array_numb_b = [int(x) for x in numb_b.split()]
    if (len(array_numb_a) == len(array_numb_b) == 2):
        return round(math.sqrt(((array_numb_b[0] - array_numb_a[0])**2) + ((array_numb_b[1] - array_numb_a[1])**2)),2)
    else:
        return 'error'
    
print('Введите координаты двух точек:')
numb_a = input('Введите координаты точки А через пробел: ')
numb_b = input('Введите координаты точки В через пробел: ')
print(number(numb_a, numb_b))