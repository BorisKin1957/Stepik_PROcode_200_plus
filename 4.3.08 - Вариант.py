from collections import defaultdict
from math import gcd



n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# if n <= 2:
#     print(n)
#     return

max_points = 1

for i in range(n):
    slopes = defaultdict(int)
    same_point = 0
    x1, y1 = points[i]

    for j in range(n):
        if i == j:
            continue
        x2, y2 = points[j]
        dx = x2 - x1
        dy = y2 - y1

        if dx == 0 and dy == 0:
            same_point += 1
        elif dx == 0:
            # вертикальная прямая
            slopes['inf'] += 1
        else:
            # нормализуем направление
            g = gcd(dx, dy)
            if dx < 0:  # приводим к каноническому виду
                dx, dy = -dx, -dy
            dx, dy = dx // g, dy // g
            slopes[(dy, dx)] += 1

    # Максимум точек на прямой через i
    current_max = max(slopes.values()) if slopes else 0
    current_max += same_point + 1  # + сама точка i
    max_points = max(max_points, current_max)

print(max_points)
