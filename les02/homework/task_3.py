# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# https://drive.google.com/file/d/11tO38EBEFZfToril6XsGHMV2uo6E-uZM/view?usp=sharing

def func(a, b):
    if a == 0:
        return b
    if a > 0:
        return func(a // 10, b * 10 + a % 10)

a = int(input("Введите натуральное число: "))

result = func(a, 0)

print(result)