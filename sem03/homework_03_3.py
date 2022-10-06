# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform, randrange

my_list = [round(uniform(0, value), 2) for value in range(1, randrange(10,20))]
new_list = [round(val%1, 2) for val in my_list]

print(new_list)
print(max(new_list) - min(new_list))