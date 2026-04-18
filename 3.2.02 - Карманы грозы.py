def merge_intervals(intervals):
    if not intervals:
        return []

    # Сортируем интервалы по началу
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        # Проверяем, можно ли объединить: current[0] <= last[1] + 1
        if current[0] <= last[1] + 1:
            # Объединяем: [last[0], max(last[1], current[1])]
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            # Нет пересечения и не касаются — добавляем как новый
            merged.append(current)

    return merged

storm_map = []
result = {}

for _ in range(int(input())):
    tmp = map(int, input().split())
    level, start, end = tmp
    window = (level, (start, end))
    storm_map.append(window)

for level, track in storm_map:
    result[level] = result.get(level, []) + [track]

for level, tracks in result.items():
    result[level] = merge_intervals(tracks)

result = sorted(result.items(), key=lambda x: (x[0], x[1]))

for level, track in result:
    for i in range(len(track)):
        print(f'{level}:{track[i][0]}-{track[i][1]}')




