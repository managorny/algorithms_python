# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
# Блок-схема https://drive.google.com/file/d/1DpTZsgaY5lA0X-1QZU5GSDOeTxrXo09h/view?usp=sharing
# Обусловлено считать пользователя идеальным, проверок на ошибки не делаем

print("Введите координаты двух точек (числа от -9 до 9, при этом координаты по оси x не должны быть равны)")
x1 = int(input("координата точки A по оси x: "))
y1 = int(input("координата точки A по оси y: "))
x2 = int(input("координата точки B по оси x: "))
y2 = int(input("координата точки B по оси y: "))

k = int((y1 - y2) / (x1 - x2))
b = int(y2 - k * x2)

if b > 0:
    print(f'y = {k}x + {b}')
elif b == 0:
    print(f'y = {k}x')
else:
    print(f'y = {k}x - {b*(-1)}')