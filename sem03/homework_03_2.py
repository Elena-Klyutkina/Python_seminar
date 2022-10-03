# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
res_list = []

for i in range(len(my_list)//2):
    res_list.append(my_list[i]*my_list[-i-1])
    
if len(my_list)%2 != 0:
    res_list.append(my_list[len(my_list)//2] ** 2)

print(res_list)


# вариант 2
# from random import randrange

# def multiplication_of_pairs(new_list):
#     right_side = new_list[int(len(new_list)/2):]
#     right_side.reverse()
#     if len(new_list)%2 !=0:
#         left_side = new_list[:int(len(new_list)/2)+1]
#     else:
#         left_side = new_list[:int(len(new_list)/2)]
#     result_list = [l_value*r_value for l_value, r_value in zip(left_side, right_side)]   
#     return result_list


# new_list = [value for value in range(1, randrange(4,20))]
# print(new_list)
# print(multiplication_of_pairs(new_list))