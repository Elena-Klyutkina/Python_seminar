# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# k=9 => 2*x^9 - 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

num = int(input("Введите натуральную степень k: "))

def magit_to_file(num: int):
    lst = []
    if num > 0:
        num1 = random.randint(0,100)   
        str_1 = f"{num1}*x^{num}"
        for i in reversed(range(2, num)):
            num1 = random.randint(0,100)    
            if num1 != 0:
                str_1 += f" + {num1}*x^{i}"
        num1 = random.randint(0,100)
        if num1 != 0:
            str_1 += f" + {num1}*x"
        num1 = random.randint(0,100)
        if num1 != 0:
            str_1 = f"{str_1} + {num1} = 0"
            lst.append(str_1)
        else:
            str_1 = print(f"{str_1} = 0")
            lst.append(str_1)
        new_str = ''.join(lst)
        print(new_str)
        new_file = open('file.txt', 'w')
        new_file.write(new_str)
       
magit_to_file(num)