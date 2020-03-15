a = float(input('Введи число a: '))
b = float(input('Введи число b: '))
c = float(input('Введи число c: '))

m = a
if m < b:
    m = b
if m < c:
    m = c

print(f'{m=}')
