'''
Шаг 1. Считай строку с нужными номерами need это числа через пробел.
Повторы игнорируются по смыслу множества.
Шаг 2. Считай целое D это число дней.
Шаг 3. Считай D строк в формате метка_дня: номера это после двоеточия идут числа
через пробел, строка может быть пустой.

Шаг 4. Найди минимальный по длине интервал индексов [L..R] с нумерацией с 1
по порядку входа, такой что объединение offer_L ∪ offer_{L+1} ∪ ... ∪ offer_R
содержит весь need.
Шаг 5. Если существует несколько интервалов минимальной длины, выбери тот,
у которого L меньше.
Шаг 6. Выведи L R. Если подходящего интервала нет, выведи Пусто.

🧪 Пример ввод

2 4 7
4
д1: 1 2
д2: 4
д3: 3 7
д4: 8


🧪 Пример вывод

1 3
'''

from itertools import combinations as cb

need = set(input().split())

D = int(input())

base = {}

for i in range(1, D + 1):
    s = input().split(': ')
    try:
        base[i] = base.get(i, set(s[1].split()))
    except IndexError:
        base[i] = set()

variants = []

s_base = dict(sorted(base.items()))

for i in range(1, D):
    var_i = list(cb(s_base.items(), r=i))
    for j in range(D):
        res = set()
        vol = var_i[j]
        days = []
        n = len(vol)
        for k in range(n):
            res |= vol[k][1]
            days.append(vol[k][0])
            if need.issubset(res):
                variants.append(days)
                continue

if variants:
    result = min(variants, key=len)
    print(result[0], result[-1])
else:
    print('Пусто')
