# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0,1,2,3,4,5,6,7,8,9]
# -> [7,5,3,4,5,2,8,6,9,0]

n = int(input('Number of elements: '))
arr = [i for i in range(n)]
print(arr)

k = -1

for i in range(len(arr)//2):
    arr[k], arr[i] = arr[i], arr[k]
print(arr)