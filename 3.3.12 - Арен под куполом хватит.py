'''
Строка 1: целое N. Далее N строк по два целых числа: start end для каждого матча.
Нужно вывести одно число это максимальное количество матчей, идущих одновременно
(минимально необходимое число арен).
🧪 Примеры ввода/вывода

Пример 1

4
0 10
2 5
5 7
7 12

2
'''

n = int(input())
events = []

for _ in range(n):
    start, end = map(int, input().split())
    events.append((start, 1))
    events.append((end, -1))

# Сортируем по времени; при равенстве — сначала -1 (окончание), потом +1 (начало)
events.sort(key=lambda x: (x[0], x[1]))

current = 0
max_matches = 0

for time, event_type in events:
    current += event_type
    if current > max_matches:
        max_matches = current

print(max_matches)