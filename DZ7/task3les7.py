# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой – не больше медианы.
# Задачу решал без сортировки исходного массива, итерацией по "срезам" между максимумом и минимумом. На четном
# размере массива алгоритм завершает работу с небольшим смещением

from random import randint


def avg_between_minmax(a, pmn, pmx):  # среднее значение элементов между pmn и pmx
    i, s = 0, 0
    for item in a:
        if pmn <= item <= pmx:
            i += 1
            s += item
    return s / i if i > 0 else float('inf')


def snapshot(a, pmn, pmx):  # профиль массива по срезу pmn, pmx
    lft, mdl, rght = 0, 0, 0
    mid_it, mid_dif = None, False  # blank for: arbitrary body member, different value body sign
    for item in a:
        if item < pmn:    # left tail size
            lft += 1
        elif item > pmx:  # right tail size
            rght += 1
        else:             # central body size & props
            if mid_it is None:
                mid_it = item
            elif mid_it != item:
                mid_dif = True
            mdl += 1
    # 0-left tail, 1-body, 2-right tail, 3-different value body, 4-body member
    return lft, mdl, rght, mid_dif, mid_it


arr = [randint(0, 10000) for i in range(100001)]  # randint(0, 10)
# arr = [6]*99 + [1, 2, 100]
# arr = [i**2 for i in range(1001)]*2
mn = min(arr)
mx = max(arr)
tails = (0, len(arr), 0, mn != mx, mn)

while tails[3]:  # пока в середине есть различные элементы
    avg = avg_between_minmax(arr, mn, mx)
    sl1 = snapshot(arr, mn, avg)
    sl2 = snapshot(arr, avg, mx)

    if sl1[0] <= len(arr) // 2 and sl1[2] <= len(arr) // 2:  # балансируем хвосты
        tails = sl1
        mx = avg
    else:
        tails = sl2
        mn = avg

print(f'\nМедианный элемент со значением {tails[4]} встречается {tails[1]} раз'
      f'\n{tails[0]} элементов меньше него, {tails[2]} элементов больше него')
print(f'\nПроверка: {sorted(arr)[len(arr)//2]}')








