"""
Написать программу сложения и *умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
*произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

six_numbs = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

fst_num = deque(input("Введите первое 16-тиричное число\n"))
snd_num = deque(input("Введите второе 16-тиричное число\n"))

fst_num.reverse()
print(fst_num)
snd_num.reverse()
print(snd_num)

# сложение
y = 0
res_sum = deque()
if len(fst_num) <= len(snd_num):
    bigger_deque = fst_num
else:
    bigger_deque = snd_num
print(bigger_deque)
for i in range(len(bigger_deque)):
    if (six_numbs.index(fst_num[i]) + six_numbs.index(snd_num[i])) > len(six_numbs):
        x = (six_numbs.index(fst_num[i]) + six_numbs.index(snd_num[i])) - len(six_numbs) + y
        y = 1
    else:
        x = (six_numbs.index(fst_num[i]) + six_numbs.index(snd_num[i])) + y
        y = 0
    res_sum.appendleft(six_numbs[x])
if (six_numbs.index(fst_num[-1]) + y) >= len(six_numbs):
    x = (six_numbs.index(fst_num[-1]) + y) - len(six_numbs)
    y = 1
    res_sum.extendleft([x, y])
elif len(fst_num) < len(snd_num):
    res_sum.appendleft(snd_num[-1])
elif len(fst_num) > len(snd_num):
    res_sum.appendleft(fst_num[-1])
else:
    res_sum.appendleft(y)

print(f'Сумма чисел равна: {res_sum}')


# TODO: умножение
