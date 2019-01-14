# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import randint

arr1 = [randint(-5,11) for _ in range(10)]
print('Inintial array:')
for v in arr1:
    print(f'{v:>3}', end=' ')

max_neg_index = -1
for i, v in enumerate(arr1):
    if arr1[i] < 0:
        if max_neg_index == -1:
            max_neg_index = i
            max_neg = arr1[i]
        else:
            if arr1[i] > max_neg:
                max_neg_index = i
                max_neg = arr1[i]

if max_neg_index == -1:
    print('\nNot found any, try again sometime :)')
else:
    print(f'\nMaximum negatve is: {arr1[max_neg_index]}'\
          f' with index {max_neg_index}')

