# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

n = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x - 1)
arr = list( f(i) for i in range(1, n + 1))
print(arr)