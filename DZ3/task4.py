# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

arr1 = [randint(0,10) for _ in range(14)]
print('Inintial array:')
for v in arr1:
    print(f'{v:>2}', end=' ')

max_cnt_index = -1
max_cnt = 0
for index, value in enumerate(arr1):
    cnt = 0
    for i, v in enumerate(arr1):
        if arr1[index] == arr1[i]:
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        max_cnt_index = index 

print(f'\nMost frequent value is: {arr1[max_cnt_index]}'\
      f' (duplicated {max_cnt} times)')


