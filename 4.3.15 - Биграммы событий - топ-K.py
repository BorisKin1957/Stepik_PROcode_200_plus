

'''
Считай целое n.

Считай n строк вида ts type, где ts -- время (порядок строк уже неубывающий),
type -- строка без пробелов. Соседние строки образуют пары типов.

Считай целое K.

Построй все пары (t_i, t_{i+1}) и посчитай их частоты.

Выведи до K строк в формате t1>t2: count в порядке:

по убыванию count;

при равенстве -- по возрастанию t1;

при равенстве -- по убыванию t2.

Если пар нет (n < 2) -- выведи -.

🧪 Пример 1 — ввод

6
00:00 A
00:01 B
00:02 A
00:03 B
00:04 B
00:05 A
2


🧪 Пример 1 — вывод

A>B: 2
B>A: 2
'''

n = int(input())

if n < 2:
    print('-')
    exit()

events = [input().split() for _ in range(n)]
k = int(input())

result = {}

for i in range(n - 1):
    ts_1, type_1 = events[i][0], events[i][1]
    ts_2, type_2 = events[i + 1][0], events[i + 1][1]
    key = f'{type_1}>{type_2}'
    result[key] = result.get(key, 0) + 1

result = sorted(result.items())#, key=lambda x: (-x[1], x[0]))
print(result)
result = sorted(result, key=lambda x: (x[1], x[0][x[0].index('>') + 1]), reverse=True)
print(result)

for event in result[:k]:
    print(f'{event[0]}: {event[1]}')
