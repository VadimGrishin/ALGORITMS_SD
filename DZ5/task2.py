from collections import deque
from random import randint

digit = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
digit_val = dict((digit[i],i) for i in range(len(digit)))

def add_nn(x, y):
    dq = deque()
    shift = '0'
    while x or y:
        s = digit_val[x.pop() if x else '0'] + digit_val[y.pop() if y else '0'] + digit_val[shift]
        dq.appendleft(digit[s % len(digit)])
        shift = digit[s // len(digit)]

    if digit_val[shift]:
        dq.appendleft(shift)

    return list(dq)

def _mult_dn(d, n):
    # Умножение цифры на число
    dq = deque()
    shift = '0'
    while n:
        s = digit_val[d] * digit_val[n.pop() if n else '0'] + digit_val[shift]
        dq.appendleft(digit[s % len(digit)])
        shift = digit[s // len(digit)]

    if digit_val[shift]:
        dq.appendleft(shift)

    return list(dq)

def mult_nn(x, y):
    shift = []
    s = []
    while y:
        a = _mult_dn(y.pop(), x[::1])
        s = add_nn(a + shift, s)
        shift += ['0']
        
    return s    

#Проверка------------------------------------------------------------
def test():
    for i in range(3):
        a = randint(0,16**4)
        aa = list(format(a,'x').upper())
        b = randint(0,16**5)
        bb = list(format(b,'x').upper())
        print(f'adec={a} ahex={aa}, \nbdec={b} bhex={bb}')
        
        t = add_nn(aa, bb)
        tt = list(format(a + b,'x').upper())
        
        print(f'my func ={t}\nbuilt-in={tt}')
            
        assert t == tt
        print('Тест OK')
        print('----------------')

def test_m():
    for i in range(3):
        a = randint(1,16**4)
        aa = list(format(a,'x').upper())
        b = randint(0,16**5)
        bb = list(format(b,'x').upper())
        print(f'adec={a} ahex={aa}, \nbdec={b} bhex={bb}')
        
        t = mult_nn(aa, bb)
        tt = list(format(a * b,'x').upper())
        
        print(f'my func ={t}\nbuilt-in={tt}')
            
        assert t == tt
        print('Тест OK')
        print('----------------')
print('Сложение тест ' + '-' * 50)
test()
print('Умножение тест ' + '-' * 50)
test_m()
#------------------------------------------------------
a = list(input('Введите шестнадцатеричное число ').upper())
b = list(input('Введите шестнадцатеричное число ').upper())
print(f'Сумма чисел {add_nn(a[::1], b[::1])}')
print(f'Произведение чисел {mult_nn(a, b)}')



