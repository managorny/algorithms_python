"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# нахождение минимума
pos = len(array)
a = array[pos - 1]
pos_d = 0
for i in array:
    pos -= 1
    if a >= i:
        a = i
        pos_d = (len(array) - 1) - pos
d_min = a
pos_d_min = pos_d
print(f'{d_min} - min')

# нахождение максимума
pos = len(array)
a = array[pos - 1]
pos_e = 0
for i in array:
    pos -= 1
    if a <= i:
        a = i
        pos_e = (len(array) - 1) - pos
e_max = a
pos_e_max = pos_e
print(f'{e_max} - max')

# вычисление суммы
if (pos_d_min - pos_e_max) > 1 or (pos_e_max - pos_d_min) > 1:
    if pos_d_min > pos_e_max:
        sum_digits = array[pos_e_max + 1]
        for k in array[pos_e_max + 2:pos_d_min]:
            sum_digits = sum_digits + k
        print(f'Сумма чисел между min и max равна {sum_digits}')
    else:
        sum_digits = array[pos_d_min + 1]
        for k in array[pos_d_min + 2:pos_e_max]:
            sum_digits = sum_digits + k
        print(f'Сумма чисел между min и max равна {sum_digits}')
else:
    sum_digits = 0
    print(f'Сумма чисел между min и max равна {sum_digits}')