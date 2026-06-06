'''
Задание
Шаг 1. Считай строку с нужными номерами need (числа через пробел, множества по смыслу).
Шаг 2. Считай целое K.
Шаг 3. Считай целое M.
Шаг 4. Считай M строк формата Имя: имею (числа через пробел, строка может быть пустой).
Шаг 5. Считай целое E, затем E строк вида Имя1 - Имя2 -- пары конфликтующих друзей (симметрично).

Шаг 6. Найди совместимый набор имён (без конфликтных пар) максимального размера, такой что
| (⋃ «имею» выбранных) ∩ need | ≥ K.
Шаг 7. Выведи любой подходящий набор имён (по одному на строке).
Если решений нет -- выведи Пусто.

Примечания. Повторы чисел и имён в «имею» не влияют (используем множества).
Формат конфликтов всегда «с пробелами вокруг дефиса».

🧪 Пример 1 ввод

2 4 7 8
3
3
Ася: 2 8
Игорь: 4 7
Лена: 4 8
1
Ася - Игорь


🧪 Пример 1 вывод

Ася
Лена
'''

from itertools import combinations as cb

need = set(input().split())
k, m = int(input()), int(input())

offers = {}

for i in range(m):
    s = input().split(': ')
    name = s[0]
    if len(s) > 1:
        st = set(s[1].split())
        st &= need
    else:
        st = set()
    offers[name] = st

e = int(input())

pairs = []

for i in range(e):
   name1, name2  = sorted(input().split(' - '))
   pairs.append(set([name1, name2]))


variants = []

for i in range(1, m + 1):
    lst = list(cb(offers.keys(), r=i))
    for j in range(len(lst)):
        variants.append(set(lst[j]))

variants.sort(key=len, reverse=True)

result = []

for names in variants:
    for pair in pairs:
        if names & pair == pair:
            names -= pair
    names = sorted(names)

    if len(names) > 1:
        result.append(names)

result.sort(key=len, reverse=True)

if result:
    for names in result:
        res = set()
        for i in range(len(names)):
            res |= offers[names[i]]
        if len(res) >= k:
            print(*names, sep='\n')
            exit()
else:
    print('Пусто')




