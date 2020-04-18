# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

n = int(input('Введите количество компаний '))
company = collections.Counter()
for i in range(n):
    sum_ = 0
    name = input('Введите название компании ')
    for j in range(4):
        sum_ += int(input(f'Введите прибыль за {j + 1} квартал '))
    company[name] = sum_

avg = sum(company.values()) / n
high = collections.deque()
low = collections.deque()
for el in company:
    if company[el] > avg:
        high.append(el)
    elif company[el] < avg:
        low.append(el)

print(f'Прибыль выше среднего у компаний {", ".join(list(high))}')
print(f'Прибыль ниже среднего у компаний {", ".join(list(low))}')