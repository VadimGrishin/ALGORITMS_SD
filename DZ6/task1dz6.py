# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Выбрано задание 6 из дз 3 и варианты ее реализации из дз 4

# Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
# 64-разрядная ОС, процессор х64

# В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from sys import getsizeof
from sys import setrecursionlimit
from collections import defaultdict
from inspect import stack

setrecursionlimit(10**4)

# 1) Вариант исходный из ДЗ3, но вычисления отделены от вывода:
def sbetween_maxmin_source(arr):
    def zero_all_prev(index, b):
        # Функция для очистки элементов массива peak_pit (карты экстремумов)
        # со значением b. Применяется при неподтверждении предыдущей гипотезы
        # об экстремальности
        for i in range(index):
            if peak_pit[i] == b:
                peak_pit[i] = 0

    # Составление карты экстремумов (пиков и впадин) в массив peak_pit
    peak_pit = [0 for i in range(len(arr))]  # заготовка для карты экстремумов
    res = []
    min_index = -1  # начальная гипотеза минимальности
    max_index = -1  # начальная гипотеза максимальности
    for index, value in enumerate(arr):
        if value < arr[min_index]:
            min_index = index  # новая гипотеза минимальности
            peak_pit[index] = -1
            zero_all_prev(index, -1)
        elif value == arr[min_index]:
            peak_pit[index] = -1

        if value > arr[max_index]:
            max_index = index  # новая гипотеза максимальности
            peak_pit[index] = 1
            zero_all_prev(index, 1)
        elif value == arr[max_index]:
            peak_pit[index] = 1
    # Коррекция [0]-го элемента карты (в случае равенства 1-го и
    # последнего элемента глобальному минимуму)
    if arr[0] <= arr[min_index]:
        peak_pit[0] = -1

        # Расчет сумм между экстремумами разных типов
    beg_slope_ind = -1
    sum_between = 0
    for i, v in enumerate(peak_pit):
        if v != 0:
            if beg_slope_ind > -1:
                if peak_pit[beg_slope_ind] * peak_pit[i] == -1:
                    # res=[[начало склона, конец склона, сумма по склону],...]:
                    res.append([beg_slope_ind, i, sum_between])
            beg_slope_ind = i
            sum_between = 0
        else:
            sum_between += arr[i]

    # анализ памяти начало -------------------------------------------
    var_names = list(locals().keys())
    cur_var = []
    for i in range(len(var_names)):
        cur_var.append(locals()[var_names[i]])
    mem_review(stack()[0][3], var_names, cur_var)
    # анализ памяти конец ---------------------------------------------

    return res

#2) Вариант 2 - использование агрегатных функций
def sbetween_maxmin_af(arr):

    res = []
    mx = max(arr)
    mn = min(arr)
    # Расчет сумм между экстремумами разных типов
    beg_slope_ind = -1
    sum_between = 0
    for i, v in enumerate(arr):
        if v in (mx, mn):
            if beg_slope_ind > -1:
                if (arr[beg_slope_ind] - arr[i]) != 0:
                    # res=[[начало склона, конец склона, сумма по склону],...]:
                    res.append([beg_slope_ind, i, sum_between])
            beg_slope_ind = i
            sum_between = 0
        else:
            sum_between += arr[i]

    # анализ памяти начало -------------------------------------------
    var_names = list(locals().keys())
    cur_var = []
    for i in range(len(var_names)):
        cur_var.append(locals()[var_names[i]])
    mem_review(stack()[0][3], var_names, cur_var)
    # анализ памяти конец ---------------------------------------------

    return res

# -------------------------------------------------------------
# 3) Вариант 3 - с использованием рекурсии:
def sbetween_maxmin_rec(arr1):
    def fill_peak_pit(n):
        nonlocal mn, mx, peak, pit
        # Составление карты экстремумов (пиков и впадин) в массивы peak, pit
        if n == 1:
            mn = min(arr1[0], arr1[1])
            mx = max(arr1[0], arr1[1])
            if arr1[0] > arr1[1]:
                peak[0], pit[1] = 1, 1
            elif arr1[0] < arr1[1]:
                peak[1], pit[0] = 1, 1
        else:
            fill_peak_pit(n - 1)

        if arr1[n] <= mn:
            if arr1[n] < mn:
                pit = [0] * len(arr1)
                mn = arr1[n]
            pit[n] = 1
        elif arr1[n] >= mx:
            if arr1[n] > mx:
                peak = [0] * len(arr1)
                mx = arr1[n]
            peak[n] = 1
    
    mn = 0
    mx = 0
    peak = [0] * len(arr1)
    pit = [0] * len(arr1)

    fill_peak_pit(len(arr1) - 1)
    peak_pit = [peak[i] - pit[i] for i in range(len(pit))]
    # Расчет сумм между экстремумами разных типов
    res = []
    beg_slope_ind = -1
    sum_between = 0
    for i, v in enumerate(peak_pit):
        if v != 0:
            if beg_slope_ind > -1:
                if peak_pit[beg_slope_ind] * peak_pit[i] == -1:
                    # res=[[начало склона, конец склона, сумма по склону],...]:
                    res.append([beg_slope_ind, i, sum_between])
            beg_slope_ind = i
            sum_between = 0
        else:
            sum_between += arr1[i]

    # анализ памяти начало -------------------------------------------
    var_names = list(locals().keys())
    cur_var = []
    for i in range(len(var_names)):
        cur_var.append(locals()[var_names[i]])
    mem_review(stack()[0][3], var_names, cur_var)
    # анализ памяти конец ---------------------------------------------

    return res

def mem_review(func_name, var_names, cur_var):
    """
    Измерение объема памяти, занятой переменными cur_var
    """
    var_ids = set() # для исключения повторного учета постоянных объектов (малых чисел, интернированных строк и т.п)
    s = 0
    mem4var = []
    print(f'\nИспользование памяти функцией {func_name}. По переменным:')
    for i in range(len(var_names)):
        if id(cur_var[i]) in var_ids:
            mem4var.append([var_names[i], 0])
            continue
        var_ids.add(id(cur_var[i]))
        mem4var.append([var_names[i], getsizeof(cur_var[i])])
        s += getsizeof(cur_var[i])
        if hasattr(cur_var[i], '__iter__'): # Объекты внутри iterable-переменной
            if not isinstance(cur_var[i], str):
                for item in cur_var[i]:
                    if id(item) in var_ids:
                        continue
                    var_ids.add(id(item))
                    mem4var[i][1] += getsizeof(item)
                    s += getsizeof(item)
    mem4var.sort(key=lambda k: k[1], reverse=True) # сортировка по размеру, desc
    print(f'{mem4var}')
    print(f'Итого {func_name}: {s / 1024: .2f} KB')
    

sbetween_maxmin_source([i%10 for i in range(0, 2*10**3)])
sbetween_maxmin_af([i%10 for i in range(0, 2*10**3)])
sbetween_maxmin_rec([i%10 for i in range(0, 2*10**3)])
