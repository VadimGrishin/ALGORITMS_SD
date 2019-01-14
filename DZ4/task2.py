from math import log
import cProfile

# 1) Решето:-------------------------------------------
def sieve(k):
    def max_prime_num():
        # max (Prime num in array) if num < k  else k
        nonlocal result
        snum = 0
        for  v in a:
            if v > 0:
                snum += 1
                if snum == k:
                    result = v # сохраняем искомое число
                    break
        return snum

    def expand_a(nnew):
        # расширение массива до размера nnew
        nonlocal a
        d = [i for i in range(len(a),nnew)]
        a += d
        
    result = 0
    #первоначальная оценка размера массива - см. теорему о распределении простых чисел:
    n = (k + 2) * int(log(k + 2) * 1.3) 
    a = [0, 0]
    expand_a(n)

    m = 2

    while True:
        while m <= n // 2: 
            if a[m] != 0: 
                j = m * 2 
                while j < n:
                    a[j] = 0 
                    j = j + m 
            m += 1

        if max_prime_num() < k: # повторить расчет, расширив массив
            m = 2
            n = int(len(a) * 1.3)
            expand_a(n)
        else:
            break
  
    return result
# cProfile.run('sieve(10**i)')
# 1    0.000    0.000    0.000    0.000 task2.py:4(sieve) --- 10
# 1    0.001    0.001    0.001    0.001 task2.py:4(sieve) --- 100
# 1    0.011    0.011    0.012    0.012 task2.py:4(sieve) --- 1000
# 1    0.096    0.096    0.113    0.113 task2.py:4(sieve) --- 10000
# 1    1.469    1.469    1.723    1.723 task2.py:4(sieve) --- 100000
# 1   19.685   19.685   22.710   22.710 task2.py:4(sieve) --- 1000000
# 1   42.606   42.606   49.057   49.057 task2.py:4(sieve) --- 2000000
# python -m timeit -n 10 -s "import task2" "task2.sieve(1000)   10 loops, best of 5: 6.29 msec per loop
# python -m timeit -n 10 -s "import task2" "task2.sieve(10000)  10 loops, best of 5: 99.2 msec per loop
# python -m timeit -n 10 -s "import task2" "task2.sieve(100000) 10 loops, best of 5: 1.5 sec per loop

#Вывод: на графике в Excel небольшая выпуклость заметна, но значительно меньше, чем для not_sieve
#Википедия говорит, что это O(lnln n) - на нее и похоже

# 2) Не решето:-------------------------------------------
def not_sieve(k):
    def divider(n):
        i = 2
        j = 0 # флаг
        while i**2 <= n and j != 1:
            if n%i == 0:
                j = 1
            i += 1
        if j == 1:
            return False
        else:
            return True
    i = 0
    cur = 1
    while i < k:
        cur += 1
        if divider(cur):
            i += 1
    return cur
# 28     0.000    0.000    0.000    0.000 task2.py:59(divider)  --- 10
# 540    0.003    0.000    0.003    0.000 task2.py:59(divider)  --- 100
# 7918   0.084    0.000    0.084    0.000 task2.py:59(divider)  --- 1000
# 27448  0.460    0.000    0.460    0.000 task2.py:59(divider)  --- 3000
# 104728 2.730    0.000    2.730    0.000 task2.py:59(divider)  --- 10000
# 350376 14.687    0.000   14.687    0.000 task2.py:59(divider) --- 30000
# python -m timeit -n 10 -s "import task2" "task2.not_sieve(1000)  10 loops, best of 5: 85.8 msec per loop
# python -m timeit -n 10 -s "import task2" "task2.not_sieve(3000)  10 loops, best of 5: 447 msec per loop
# python -m timeit -n 10 -s "import task2" "task2.not_sieve(10000) 10 loops, best of 5: 2.75 sec per loop

# Вывод: здесь выпуклость значительно больше, и простая оценка дает:
#    sum(sqrt(i)), i от 1 до n = O(n**1.5). Линия тренда в Excel дала оценку 3Е-6*(n**1.492)
# Применяем sieve, он лучше


## Проверка ----------------------------------------------------------------------------------
##i=2
##print(f'{i:>3} {not_sieve(i)}')
##for i in range(1,30):
##    print(f'{i:>3} {not_sieve(i)} {sieve(i)}')
##cProfile.run('sieve(50000)')
##for i in range(1,5):
##    print('-----------------')
##    print(10**i)
##    cProfile.run('not_sieve(10**i)')

