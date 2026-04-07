'''
🎯 Задание
Разбор строки маршрута с якорями '#' и применение циклического сдвига к каждому сегменту.
'''

# Считываем маршрут и разбиваем по символу '#'
segments = [segment.split() for segment in map(str.strip, input().split('#'))]

# Считываем сдвиги
shifts = list(map(int, input().split()))
length = len(shifts)  # количество сегментов

route = []  # итоговый маршрут: список списков (токены и ['#'])

for i in range(length):
    n = len(segments[i])  # длина текущего сегмента

    # Если сегмент не пустой — применяем циклический сдвиг вправо
    if n > 0:
        shift = shifts[i] % n
        if shift != 0:
            segments[i] = segments[i][-shift:] + segments[i][:-shift]

    # Добавляем текущий сегмент (может быть пустым)
    route.append(segments[i])

    # Добавляем якорь '#' после сегмента, если он не последний
    if i < length - 1:
        route.append(['#'])

# Формируем финальный вывод
output_parts = []
for part in route:
    if part == ['#']:
        output_parts.append('#')
    else:
        output_parts.extend(part)

print(' '.join(output_parts))