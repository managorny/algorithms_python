# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# Блок-схема https://drive.google.com/file/d/1DpTZsgaY5lA0X-1QZU5GSDOeTxrXo09h/view?usp=sharing
# Обусловлено считать пользователя идеальным, проверок на ошибки не делаем

input('Введите три разных числа (нажмите Enter для продолжения)')
a = float(input('Первое: '))
b = float(input('Второе: '))
c = float(input('Третье: '))

if c < a < b or b < a < c:
    print('Среднее число: ', a)
elif c < b < a or a < b < c:
    print('Среднее число: ', b)
else:
    print('Среднее число: ', c)