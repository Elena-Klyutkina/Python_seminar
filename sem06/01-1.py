# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# def IntInput(message):
#     result = -1
#     while result:
#         try:
#             result = int(input(message))
#         except:
#             print('Введено не число')
#             result = -1
#         finally:
#             return result
        
# dayNumber = -1
# while dayNumber:
#     dayNumber = IntInput('Введите номер недели: ')
#     if 1 <= dayNumber <= 5:
#         print('Нет')
#     elif 6 <= dayNumber <= 7:
#         print('Да')
#     elif dayNumber != 0:
#         dayNumber = -1

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
                 
day_numbers = [1, 2, 3, 4, 5, 6, 7]
day_names = ['Рабочий день', 'Рабочий день', 'Рабочий день', 'Рабочий день', 'Рабочий день', 'Выходной день', 'Выходной день']
zipped = zip(day_numbers, day_names)
d = list(zipped)

dayNumber = IntInput('Введите номер дня недели: ')
if 1 <= dayNumber <= 5:
    print(d[dayNumber - 1])
elif 6 <= dayNumber <= 7:
    print(d[dayNumber - 1])
else:
    print('Введен некорректный номер дня недели')