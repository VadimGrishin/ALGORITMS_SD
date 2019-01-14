#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# любому из чисел в диапазоне от 2 до 9.
print('In the range [2, 99]:')
for i in range(2, 10):
    print(f'{99 // i} numbers are multiples of {i}')

