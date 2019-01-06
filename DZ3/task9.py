# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

matrix = [[randint(-10,10) for _ in range(5)] for _ in range(3)]

for j in range(len(matrix[0])):
    colmin = matrix[0][j]
    for i in range(len(matrix)):
        if matrix[i][j] <= colmin:
            colmin = matrix[i][j]
            min_i = i
            min_j = j
    if j == 0 or colmin >= maximin:
        maximin = colmin
        maximin_i = min_i
        maximin_j = min_j

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f'{matrix[i][j]:>4}', end = '')
    print()

print(f'\n Maximin a[{maximin_i}][{maximin_j}] = {maximin}')
    

            
    
