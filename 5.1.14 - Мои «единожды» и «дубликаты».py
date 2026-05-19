

from collections import Counter

try:
    numbers = Counter(input().split())
except EOFError:
    print('Уникальные: -\nДубликаты: -')
    exit()

uniq = sorted([int(key) for key in numbers if numbers[key] == 1])

if uniq:
    print(f'Уникальные: {' '.join(map(str, uniq))}')
else:
    print('Уникальные: -')

double = sorted([int(key) for key in numbers if numbers[key] > 1])

if double:
    print(f'Дубликаты: {' '.join(map(str, double))}')
else:
    print('Дубликаты: -')