# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка
# должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
from random import randint

array = [randint(-100, 99) for i in range(15)]
print(array)
n = 1
while n < len(array):
    permut_count = 0
    for i in range(len(array) - n):  # нет смысла проверять уже всплывшие пузырьки
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            permut_count += 1        
    if permut_count == 0:  # заканчиваем, если ничего не всплыло
        break
    n += 1

print(array)
