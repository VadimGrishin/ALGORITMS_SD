# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform


def my_rand(x, y):
    res = uniform(x, y)
    return res if res < y else x


a = [my_rand(0, 50) for i in range(10)]


def merge_sort(arr):
    larr = len(arr)
    if larr == 1:
        return arr
    else:
        m = len(arr) // 2
        parts = merge_sort(arr[:m]), merge_sort(arr[m:])
    res = []
    i, j = 0, 0
    while i < m and j < larr - m:
        if parts[0][i] < parts[1][j]:
            res.append(parts[0][i])
            i += 1
        elif parts[0][i] > parts[1][j]:
            res.append(parts[1][j])
            j += 1
        elif parts[0][i] == parts[1][j]:
            res.append(parts[0][i])
            res.append(parts[1][j])
            i, j = i+1, j+1

    if i < m:
        res += parts[0][i:]
    elif j < larr - m:
        res += parts[1][j:]

    return res


print(a)
print(merge_sort(a))
