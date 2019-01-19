#Взято задание 6 из ДЗ 3
# В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import cProfile
from sys import setrecursionlimit

setrecursionlimit(10000)
# -------------------------------------------------------------
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
    peak_pit = [0 for i in range(len(arr))] # заготовка для карты экстремумов
    res = []
    min_index = -1 # начальная гипотеза минимальности
    max_index = -1 # начальная гипотеза максимальности
    for index, value in enumerate(arr):
        if value < arr[min_index]:
            min_index = index # новая гипотеза минимальности
            peak_pit[index] = -1
            zero_all_prev(index, -1)
        elif value == arr[min_index]:
            peak_pit[index] = -1
            
        if value > arr[max_index]:
            max_index = index # новая гипотеза максимальности 
            peak_pit[index] = 1
            zero_all_prev(index, 1)
        elif value == arr[max_index]:
            peak_pit[index] = 1
    # Коррекция [0]-го элемента карты (в случае равенства 1-го и
    # последнего элемента глобальному минимуму)
    if arr[0] <=  arr[min_index]:
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
    return res
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_source([i%10 for i in range(0, 1000)])"     10 loops, best of 5: 634 usec per loop
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_source([i%10 for i in range(0, 2000)])"     10 loops, best of 5: 1.29 msec per loop
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_source([i%10 for i in range(0, 10000)])"    10 loops, best of 5: 6.48 msec per loop
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_source([i%10 for i in range(0, 100000)])"   10 loops, best of 5: 67.5 msec per loop
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_source([i%10 for i in range(0, 1000000)])"  10 loops, best of 5: 742 msec per loop

#test_arr = [i%10 for i in range(0, 1000)] ---  1    0.001    0.001    0.001    0.001 task1.py:12(sbetween_maxmin_source)
#test_arr = [i%10 for i in range(0, 2000)] ---  1    0.002    0.002    0.002    0.002 task1.py:12(sbetween_maxmin_source)
#test_arr = [i%10 for i in range(0, 10000)] --- 1    0.005    0.005    0.006    0.006 task1.py:12(sbetween_maxmin_source)
#test_arr = [i%10 for i in range(0, 100000)] ---1    0.060    0.060    0.068    0.068 task1.py:12(sbetween_maxmin_source)
#test_arr = [i%10 for i in range(0, 1000000)]---1    0.629    0.629    0.730    0.730 task1.py:12(sbetween_maxmin_source)

# Вывод: сложность O(n). На самом деле, при более сложных входных данных - с монотонным изменением экстремумов сложность
# будет увеличиваться до O(n**2) за счет вызовов zero_all_prev при изменении гипотез экстремальности (Sum(i), i от 1 до n ~ n**2/2)

# -------------------------------------------------------------
#2) Вариант 2 - использование агрегатных функций (уже можно, ура!)
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
    return res
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_af([i%10 for i in range(0, 1000)])"    10 loops, best of 5: 410 usec per loop
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_af([i%10 for i in range(0, 2000)])"    10 loops, best of 5: 830 usec per loop
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_af([i%10 for i in range(0, 10000)])"   10 loops, best of 5: 4.26 msec per loop
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_af([i%10 for i in range(0, 100000)])"  10 loops, best of 5: 43.5 msec per loop
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_af([i%10 for i in range(0, 1000000)])" 10 loops, best of 5: 475 msec per loop

#test_arr = [i%10 for i in range(0, 1000)] ---  1    0.000    0.000    0.000    0.000 task1.py:67(sbetween_maxmin_af)
#test_arr = [i%10 for i in range(0, 2000)] ---  1    0.001    0.001    0.001    0.001 task1.py:69(sbetween_maxmin_af)
#test_arr = [i%10 for i in range(0, 10000)] --- 1    0.006    0.006    0.007    0.007 task1.py:70(sbetween_maxmin_af)
#test_arr = [i%10 for i in range(0, 100000)] ---1    0.033    0.033    0.041    0.041 task1.py:71(sbetween_maxmin_af)
#test_arr = [i%10 for i in range(0, 1000000)]---1    0.351    0.351    0.433    0.433 task1.py:72(sbetween_maxmin_af)

# Вывод: сложность O(n). Наиболее эффективный из трех алгоритмов, что и кодом программы подтверждается

# -------------------------------------------------------------
#3) Вариант 3 - с использованием рекурсии (чисто для тренировки):
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
            

    mn=0
    mx=0
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
    return res
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_rec([i%10 for i in range(0, 1000)])"     10 loops, best of 5: 940 usec per loop
#python -m timeit -n 10 -s "import task1" "task1.sbetween_maxmin_rec([i%10 for i in range(0, 2000)])"     10 loops, best of 5: 2.22 msec per loop
#увы, timeit отказался работать для "task1.sbetween_maxmin_rec([i%10 for i in range(0, 3000)])", хотя setrecursionlimit(10000)

#test_arr = [i%10 for i in range(0, 1000)] ---    999/1    0.002    0.000    0.002    0.002 task1.py:96(fill_peak_pit) 
#test_arr = [i%10 for i in range(0, 2000)] ---   1999/1    0.004    0.000    0.004    0.004 task1.py:99(fill_peak_pit)
#cProfile тоже отказал

#Вывод: увы, рекурсия не тянет (. Рекурсия одномерная, поэтому оптимизировать при помощи кэширования не получится

# ---------------------------------------------------------------------------------
# тестирование алгоритмов
def test_sbetween(func):
    arr1 = [1, 2,  3,  6, 2,  1,  6, 1]
    result = func(arr1)
    # res=[[начало склона, конец склона, сумма по склону],...]:
    assert result == [[0,3,5], [3,5,2],[5,6,0],[6,7,0]], f'Работает некорректно {result}'
    print(f'Работает корректно {result}')
    
##print('1) Исходный код из ДЗ: ', end='')
##test_sbetween(sbetween_maxmin_source)
##print('2) Вариант с агрегатными функциями: ', end='')
##test_sbetween(sbetween_maxmin_af)
##print('3) Вариант 3 - с использованием рекурсии: ', end='')
##test_sbetween(sbetween_maxmin_rec)
##print()

##test_arr = [i%10 for i in range(0, 1000000)]
##cProfile.run('sbetween_maxmin_source(test_arr)')
##cProfile.run('sbetween_maxmin_af(test_arr)')
##cProfile.run('sbetween_maxmin_rec(test_arr)')








