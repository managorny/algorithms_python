"""
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict


def func(x):
    quarters = 4
    d = 0
    s_list = []
    for i in range(x):
        a = input(f'Введите название компании {i + 1}:\n')
        q = 1
        while q <= quarters:
            c = int(input(f'Введите прибыль компании {a} за {q} квартал:\n'))
            q += 1
            d = d + c
            s_list.append((a, c))
    return d / x, s_list


mid_profit, spam_list = func(int(input(f'Введите количество предприятий:\n')))

print(f'Средняя прибыль для всех компаний: {mid_profit}')

our_dict = defaultdict(list)
for company, profit in spam_list:
    our_dict[company].append(profit)

up_mid_profit = []
down_mid_profit = []
for k in our_dict:
    if sum(our_dict[k]) > mid_profit:
        up_mid_profit.append(k)
    elif sum(our_dict[k]) < mid_profit:
        down_mid_profit.append(k)

if up_mid_profit:
    print(f'Выше среднего прибыль у компаний:')
    for k in up_mid_profit:
        print(k)
elif down_mid_profit:
    print(f'Ниже среднего прибыль у компаний:')
    for k in down_mid_profit:
        print(k)
else:
    print(f'У всех компаний прибыль равна средней прибыли')
