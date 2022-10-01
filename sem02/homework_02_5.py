# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0,1,2,3,4,5,6,7,8,9]
# -> [7,5,3,4,1,2,8,6,9,0]

import os
import random

# # Очистка терминала для удобства восприятия.
os.system('cls')

# # Реализуйте алгоритм перемещения списка. Без функции shuffle из модуля random

basic_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Исходный массив:\n {basic_array}')

random_array = []
for i in range(len(basic_array)):
    random_array.append(basic_array.pop(random.randint(0, len(basic_array)-1)))
print(f'Перемешанный массив:\n {random_array}')