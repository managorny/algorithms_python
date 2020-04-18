"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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
print(f'{d_min} - минимум в позиции - {pos_d_min}')

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
print(f'{e_max} - максимум в позиции - {pos_e_max}')

# смена местами минимума и максимума
array[pos_d_min], array[pos_e_max] = array[pos_e_max], array[pos_d_min]
print(f'Смена местами:\n{array}')
