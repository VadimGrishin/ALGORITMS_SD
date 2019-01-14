# 3. В массиве случайных целых чисел поменять местами минимальный и
# максимальный элементы.

from random import randint

arr1 = [randint(-100,100) for _ in range(12)]
print('Inintial array:')
for v in arr1:
    emph = ' '  # резервная позиция под акцент (!) на измененных элементах
    print(f'{v:>4}{emph}', end=' ')

min_index = 0
max_index = 0
for index, value in enumerate(arr1):
    if value < arr1[min_index]:
        min_index = index
    elif value > arr1[max_index]:
        max_index = index

arr1[min_index], arr1[max_index] = arr1[max_index], arr1[min_index] 
print('\nResult array:')
for i, v in enumerate(arr1):
    if i in (min_index, max_index):
        emph = '!'
    else:
        emph = ' '
    print(f'{v:>4}{emph}', end=' ')

