"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
# Будем дополнять массив налету. Обращаться к нему по индексу за нужным числом.
# Пока решил, где можно задавать диапазон заранее. Т.е. есть предположение, что нужный диапазон будет в расчете
# x * 10 * число разрядов x.

import timeit
import cProfile


def sieve(x):
    count = len(str(x))
    const_num = 10*count
    n = x*const_num
    sieve = [i for i in range(n)]
    sieve[1] = 0
    res = []
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            res.append(i)
            while j < n:
                sieve[j] = 0
                j += i
    print(res)
    print(res[x-1])
    return res[x-1]


sieve(5)

# print(timeit.timeit('func(10)', number=100, globals=globals()))  # 0.0083016
# print(timeit.timeit('func(100)', number=100, globals=globals()))  # 0.15323347
# print(timeit.timeit('func(1000)', number=100, globals=globals()))  # 2.312893007
# print(timeit.timeit('func(10000)', number=100, globals=globals()))  # 39.681618003000004
# print(timeit.timeit('func(100000)', number=100, globals=globals()))  # 486.83744152400004
# cProfile.run('sieve(10)')  #         1    0.000    0.000    0.000    0.000 task_2.py:18(sieve)
# cProfile.run('sieve(100)')  #         1    0.001    0.001    0.002    0.002 task_2.py:18(sieve)
# cProfile.run('sieve(1000)')  #         1    0.023    0.023    0.027    0.027 task_2.py:18(sieve)
# cProfile.run('sieve(10000)')  #         1    0.344    0.344    0.381    0.381 task_2.py:18(sieve)
# cProfile.run('sieve(100000)')  #         1    4.543    4.543    5.046    5.046 task_2.py:18(sieve)

# 2 вариант без решета, через перебор делителей. Решен не до конца. Есть ошибки.
# def prime(x):
#     count = len(str(x))
#     const_num = 10*count
#     n = x*const_num
#     sieve = [i for i in range(n)]
#     sieve[1] = 0
#     print(sieve)
#     primes = [2, 3]
#     for i in sieve:
#         limit = i ** 0.5    # вместо sqrt(i)
#         k = 2
#         while k <= limit:
#             if i % k != 0:
#                 primes.append(i)
#                 k += 1
#             else:
#                 break
#     print(sieve)
#     print(primes)
#     print(primes[x - 1])
#
#
# prime(5)
