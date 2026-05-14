'''
Считай целое n, затем n строк с целыми координатами x y. Нужно вывести одно
число -- максимум точек, которые лежат на одной прямой
'''

from collections import defaultdict
from math import gcd

points = [tuple(map(int, input().split())) for _ in range(int(input()))]

n = len(points)
lines = []
dup = 0

for i in range(n):
    x1, y1 = points[i]
    slope = defaultdict(list)


    for j in range(i + 1, n):
        if i == j:
            continue
        x2, y2 = points[j]

        # нормализуем
        dx = x2 - x1
        dy = y2 - y1

        if dx == 0 and dy == 0: # повторяющаяся точка
            dup += 1

        if dx == 0: # вертикальная линия
            key = ('inf', x1)
        else:
            g = gcd(dx, dy)
            dx = dx // g
            dy = dy // g

            if dx < 0:
                dx, dy = -dx, -dy
            key = (dy, dx, x1, y1)
        slope[key].append(j)

    # собираем линии с >= 2 доп точками
    for key, idxs in slope.items():
        line_points = {i}
        line_points.update(idxs)
        if len(line_points) >= 3:
            lines.append(line_points)


print(len(max(lines, key=len)) + dup)

