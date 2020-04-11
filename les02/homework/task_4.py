# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/11tO38EBEFZfToril6XsGHMV2uo6E-uZM/view?usp=sharing

a = int(input("Введите кол-во элементов: "))
b = 1
c = 1

for i in range(a):
    b = b / -2
    c = c + b

print(c)