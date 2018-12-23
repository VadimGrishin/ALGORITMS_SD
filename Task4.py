# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно. 
import random
print("Выберите тип (Целое, Вещественное = число с десятичной точкой,Маленькая латинская буква) и введите 2 значения этого типа:")
a = input("Введите 1 значение: ")
b = input("Введите 2 значение: ")
if a.isalpha():
    c = chr(random.randint( ord(a), ord(b) ))
elif a.isdigit():
    c = random.randint(int(a), int(b))
else:
    c = random.uniform(float(a), float(b))
print(f'Случайное значение в ваших границах: {c}')

