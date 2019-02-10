# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from collections import Counter


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def take_next():  # забрать следующий непустой элемент из конвейера working_arr
    global cur  # указатель на текущую ячейку конвейера
    while not working_arr[cur]:
        cur += 1
    
    return cur, working_arr[cur].pop()


def tree_scan(bin_tree, path=''):  # заполнение кодировочной таблицы "мыслию по древу":)
    if bin_tree.value == -1:
        tree_scan(bin_tree.left, path=f'{path}0')
        tree_scan(bin_tree.right, path=f'{path}1')
    if bin_tree.value != -1:
        code_table[bin_tree.value] = path


string = 'dva тттттрррррриииии deviat'

char_freq = Counter(string)
working_arr = []
code_table = dict()
cur = 0
for i in range(len(string)):  # создаем конвейер размером с длину исходной строки
    working_arr.append([])

for k, v in char_freq.items():  # помещаем в него "листья" согласно их частоте
    working_arr[v - 1].append(MyNode(k))

# собираем листья в дерево
while not working_arr[-1]:  # пока не собрана вся строка (элемент, соответствующий размеру строки пуст)
    a = take_next()
    b = take_next()
    c = MyNode(-1)  # пустой узел для сборки
    c.left, c.right = a[1], b[1]
    working_arr[a[0] + b[0] + 1].append(c)  # новый узел помещаем в ячейку, соотв. его суммар. частоте

tree_scan(working_arr[-1][0])

arj_string = ''  # собственно кодировка
for c in string:
    arj_string += code_table[c]

print(f'Исходная строка:       {string}')
print(f'Закодированная строка: {arj_string}')
print('Проверка визуально:')
for c in string:
    print(f'{c:>6}', end='')
print()
for c in string:
    print(f'{code_table[c]:>6}', end='')



