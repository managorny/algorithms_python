# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Блок-схема https://drive.google.com/file/d/1DpTZsgaY5lA0X-1QZU5GSDOeTxrXo09h/view?usp=sharing
# Обусловлено считать пользователя идеальным, проверок на ошибки не делаем

input("Проведем побитовые операции \"И\" \"ИЛИ\" над числами 5 и 6\nДля продолжения нажмите Enter ")
a = 5 & 6
b = 5 | 6

print(f'Побитовая операция "И" дает результат {a}')
print(f'Побитовая операция "ИЛИ" дает результат {b}')

input("\nДалее проведем сдвиг вправо и влево числа 5\nДля продолжения нажмите Enter ")
c = 5 >> 2
d = 5 << 2

print(f'5 со сдвигом вправо = {c}')
print(f'5 со сдвигом влево = {d}')