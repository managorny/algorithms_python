# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
# https://drive.google.com/file/d/11tO38EBEFZfToril6XsGHMV2uo6E-uZM/view?usp=sharing

a = 32
b = 127
z = (b + 1) - a
x = 0

for i in range(z):
    c = a + i
    s = chr(c)
    if x < 9:
        x = x + 1
        d = '\'%s %s\'\t' % (c, s)
        print(d, end='')
    else:
        x = 0
        d = '\'%s %s\'' % (c, s)
        print(d)
