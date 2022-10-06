# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: 650 -> [2, 5, 5, 13]

def Сalculation(numb):
    multipliers = []
    mult = 2
    while mult * mult <= numb:
        if numb % mult == 0:
            multipliers.append(mult)
            numb //= mult
        else:
            mult += 1
    if numb > 1:
        multipliers.append(numb)
    return multipliers
print(Сalculation(int(input('Введите число: '))))