# 6. В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Задача решена в общем виде, т.е. без предположения 
# об уникальности пары (минимальный, максимальный).
# Находятся все возможные промежутки и суммы для каждой пары.
# Под парой понимаются ближайшие друг к другу экстремумы разных типов,
# между которыми нет других экстремумов.

from random import randint

# Функция для очистки элементов массива peak_pit (карты экстремумов)
# со значением b. Применяется при неподтверждении предыдущей гипотезы
# об экстремальности
def zero_all_prev(index, b):
    for i in range(index):
        if peak_pit[i] == b:
            peak_pit[i] = 0

SIZE = 16
arr1 = [randint(-4,4) for _ in range(SIZE)]
# arr1 = [1, 2,  3,  4,  5,  6, 1]
# arr1 = arr1[::-1]
print('Inintial array:')
for i in range(SIZE):
    print(f'{i:>3}', end=' ')
print()
for v in arr1:
    print(f'{v:>3}', end=' ')
print()
peak_pit = [0 for i in range(len(arr1))] # заготовка для карты экстремумов

# Составление карты экстремумов (пиков и впадин) в массив peak_pit
min_index = -1 # начальная гипотеза минимальности
max_index = -1 # начальная гипотеза максимальности
for index, value in enumerate(arr1):
    if value < arr1[min_index]:
        min_index = index # новая гипотеза минимальности
        peak_pit[index] = -1
        zero_all_prev(index, -1)
    elif value == arr1[min_index]:
        peak_pit[index] = -1
        
    if value > arr1[max_index]:
        max_index = index # новая гипотеза максимальности 
        peak_pit[index] = 1
        zero_all_prev(index, 1)
    elif value == arr1[max_index]:
        peak_pit[index] = 1
# Коррекция [0]-го элемента карты (в случае равенства 1-го и
# последнего элемента глобальному минимуму)
if arr1[0] <=  arr1[min_index]:
    peak_pit[0] = -1

print('Peak_pit array:')
for v in peak_pit:
    print(f'{v:>3}', end = ' ')
print()

# Расчет сумм между экстремумами разных типов
beg_slope_ind = -1
sum_between = 0
for i, v in enumerate(peak_pit):
    if v != 0:
        if beg_slope_ind > -1:
            if peak_pit[beg_slope_ind] * peak_pit[i] == -1:
                print(f'Между arr[{beg_slope_ind}] и arr[{i}] '\
                      f'сумма элементов {sum_between}')
        beg_slope_ind = i
        sum_between = 0
    else:
        sum_between += arr1[i]







