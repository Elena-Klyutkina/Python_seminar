# Напишите программу, которая принимает на вход два числа. Задайте список из N элементов, заполненных числами из промежутка [N, -N]. 
# Найдите произведение элементов, на указанных позициях (не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5,-4,-3,-2,-1,0,1,2,3,4,5]
# -> 15


# Было:
# x = int(input('Insert position one: '))
# y = int(input('Insert position two: '))

# arr_plus = [i for i in range(int(input('Number of elements: '))+1)]
# arr_minus = [-i for i in arr_plus]
# arr = arr_plus + arr_minus
# arr = list(set(arr))
# arr_new = sorted(arr)
# print(arr_new)

 
# if (0 <= x < len(arr_new)) and (0 <= y < len(arr_new)):
#     pr = arr_new[x] * arr_new[y]
#     print(pr)
# else:
#     print('Incorrect positions have been entered')
    
# Стало:    

def calc(op, a, b):
    print(op(a, b))
    
x = int(input('Insert position one: '))
y = int(input('Insert position two: '))

arr_plus = [i for i in range(int(input('Number of elements: '))+1)]
arr_minus = [-i for i in arr_plus]
arr = arr_plus + arr_minus
arr = list(set(arr))
arr_new = sorted(arr)
print(arr_new)

if (0 <= x < len(arr_new)) and (0 <= y < len(arr_new)):
    calc(lambda a, b: a * b, arr_new[x], arr_new[y])
    print(calc())
else:
    print('Incorrect positions have been entered')