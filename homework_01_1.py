# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# import isdigit
# result = input('Введите число: ')
# while result not isdigit
# number_day = int(result)

def IntInput(message):
    result = -1
    while result:
        try:
            result = int(input(message))
        except:
            print('Введено не число')
            result = -1
        finally:
            return result
        
dayNumber = -1
while dayNumber:
    dayNumber = IntInput('Введите номер недели: ')
    if 1 <= dayNumber <= 5:
        print('Нет')
    elif 6 <= dayNumber <= 7:
        print('Да')
    elif dayNumber != 0:
        dayNumber = -1