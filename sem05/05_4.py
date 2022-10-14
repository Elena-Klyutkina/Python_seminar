# Задача №41: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах. Пример:
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:          12W1B12W3B24W1B14W

data = open('file_with_data.txt', 'r')
arr = []
for line in data:
    arr.extend(line)
data.close()
count = 1
new_arr = []
for index in range(1, len(arr)):
    if arr[index-1] == arr[index] and index != len(arr)-1:
        count += 1
    elif arr[index-1] != arr[index] and index != len(arr)-1:
        new_arr.append(count)
        new_arr.append(arr[index-1])
        count = 1
    elif index == len(arr)-1:
        count += 1
        new_arr.append(count)
        new_arr.append(arr[index])
with open('file_with_newdata.txt', 'w') as new_data:
    new_data.write(''.join(map(str, new_arr)))