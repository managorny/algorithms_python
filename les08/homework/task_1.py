"""
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
func("papa")
6
func("sova")
9
"""

import hashlib


def func(string):
    res = set()
    for i in range(1, len(string)):
        for k in range(len(string) - i + 1):
            res.add(hashlib.sha1(string[k:k + i].encode('utf-8')).hexdigest())
    print(len(res))


func('papa')
