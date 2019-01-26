digit = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
digit_val = dict((digit[i], i) for i in range(len(digit)))


def add_nn(x, y, add_mult):
    # add_mult = 1 сложение чисел x и y, = 0 - умножение цифры x на число y
    res = []
    shift = '0'
    while x and add_mult or y:
        if add_mult:
            s = digit_val[x.pop() if x else '0'] + digit_val[y.pop() if y else '0'] + digit_val[shift]
        else:
            s = digit_val[x] * digit_val[y.pop() if y else '0'] + digit_val[shift]
        res = [digit[s % len(digit)]] + res
        shift = digit[s // len(digit)]

    return ([shift] if digit_val[shift] else []) + res


def mult_nn(p1, p2):
    shift = []
    s = []
    while p2:
        q = add_nn(p2.pop(), p1[::1], 0)
        s = add_nn(q + shift, s, 1)
        shift += ['0']
        
    return s    


a = list(input('Введите шестнадцатеричное число ').upper())
b = list(input('Введите шестнадцатеричное число ').upper())
print(f'Сумма чисел {add_nn(a[::1], b[::1], 1)}')
print(f'Произведение чисел {mult_nn(a, b)}')
