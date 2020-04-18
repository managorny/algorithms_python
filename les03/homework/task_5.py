"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# создаем массивы с отрицательными числами и их позициями
pos = len(array)
a = array[pos - 1]
pos_e = 0
array_2 = []
array_3 = []

for i in array:
    pos -= 1
    pos_e = (len(array) - 1) - pos
    if i < 0:
        array_2 = array_2 + [i]
        array_3 = array_3 + [pos_e]

# ищем максимальный среди отрицательных и его позицию
pos = 0
a = array_2[pos]
pos_e = 0
for i in array_2:
    if a <= i:
        a = i
        pos_e = array_3[pos]
    pos += 1

e_max = a
pos_e_max = pos_e
print(f'{e_max} максимальный отрицательный в позиции {pos_e_max}')