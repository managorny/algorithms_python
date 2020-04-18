"""
4. Определить, какое число в массиве встречается чаще всего.
"""
# Похоже, что текущее решение не совсем подходит для больших данных (вероятно из-за сравнения 2х массивов)
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# считаем какие числа встречаются чаще, записываем результаты в новый массив
array_2 = []
for i in array:
    how_often = 0
    for k in array:
        if i == k:
            how_often += 1
    array_2 = array_2 + [how_often]
pos = len(array_2)
a = array_2[pos - 1]
pos_max = 0

# ищем максимальное число повторений в исходном массиве (через второй массив)
for i in array_2:
    pos -= 1
    if a <= i:
        a = i
        pos_max = (len(array) - 1) - pos

# print(array_2)

pos_2 = 0
array_3 = []

# записываем числа, которые чаще всего повторяются в новый массив
for k in array_2:
    if k == array_2[pos_max]:
        array_3 = array_3 + [array[pos_2]]
    pos_2 += 1

# print(array_3)

# ищем уникальные в 3м массиве
# unique = set(array_3) # наверно это уже читерство
# unique = list(unique)
array_4 = [array_3[0]]
for k in array_3[1:]:
    if k not in array_4:
        array_4 = array_4 + [k]

# print(array_4)

if len(array_4) == len(array):
    print("Нет повторяющихся чисел")
else:
    print('Чаще всего встречается(ются) число(а):')
    for k in array_4:
        print(f'{k}', end='\t')
