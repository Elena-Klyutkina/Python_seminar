# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# https://docs-python.ru/packages/klient-bd-mysql/khranimye-protsedury-funktsii-bd-mysql/

num = abs(float(input('Введите число: ')))

def sum_int(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def sum_float(n):
    if n > 1:
        while n > int(n):
            n = n*10
        return n
    else:
        while n.is_integer() == False:
            n = round(n*10,5)
        return n
    
if ((num).is_integer() == True):
    print(int(sum_int(num)))
else:
    num_new = int(sum_float(num))
    # print(num_new)
    print(int(sum_int(num_new)))