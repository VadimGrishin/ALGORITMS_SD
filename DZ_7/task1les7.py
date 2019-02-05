# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка
# должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
from random import randint

array = [randint(-100, 99) for i in range(15)]
print(array)


def bubble(arr):
    n = 1
    while n < len(arr):
        permut_count = 0
        for i in range(len(arr) - n):  # нет смысла проверять уже всплывшие пузырьки
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                permut_count += 1
        if permut_count == 0:  # заканчиваем, если ничего не всплыло
            break
        n += 1
    return arr


print(bubble(array))
