a = float(input('Введи число a: '))
b = float(input('Введи число b: '))
c = float(input('Введи число c: '))

if a > b:
    if a > c:
        print(f'{a=}')
    else:
        print(f'{c=}')
else:
    if b > c:
        print(f'{b=}')
    else:
        print(f'{c=}')
