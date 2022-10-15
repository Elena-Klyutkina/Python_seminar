# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример: 
# [4, 5, 3, 3, 4, 1, 2] -> [5, 1, 2]

# from random import randint

# list = [randint(1, 10) for i in range(int(input('Введите число: ')))]
# print(f'Было: {list}')
# new_list = []
# for i in list:
#    if list.count(i) == 1:
#        new_list.append(i)
# print(f'Стало: {new_list}')

from random import randint

my_list = [randint(1, 10) for i in range(int(input('Введите число: ')))]
print(f'Было: {my_list}')

def func(x):
    if my_list.count(x) > 1:
        return False
    else:
        return True
print(f'Стало: {list(filter(func, my_list))}')