import sys

# Чтение n
try:
    line1 = sys.stdin.readline()
    if not line1:
        exit()
    n = int(line1.strip())
except ValueError:
    exit()

points = set()
xs = set()
ys = set()

for _ in range(n):
    try:
        line = sys.stdin.readline()
        if not line:
            break
        x, y = map(int, line.split())
        points.add((x, y))
        xs.add(x)
        ys.add(y)
    except ValueError:
        break

# Если точек меньше 4, прямоугольник построить нельзя
if n < 4:
    print(0)
    exit()

min_area = float('inf')
found = False

# Преобразуем множества в отсортированные списки для упорядоченного перебора
sorted_xs = sorted(list(xs))
sorted_ys = sorted(list(ys))

# Перебираем все возможные пары x (x1, x2) где x1 < x2
for i in range(len(sorted_xs)):
    for j in range(i + 1, len(sorted_xs)):
        x1 = sorted_xs[i]
        x2 = sorted_xs[j]
        width = x2 - x1

        # Перебираем все возможные пары y (y1, y2) где y1 < y2
        for k in range(len(sorted_ys)):
            for l in range(k + 1, len(sorted_ys)):
                y1 = sorted_ys[k]
                y2 = sorted_ys[l]
                height = y2 - y1

                # Проверяем, есть ли все 4 угла в множестве точек
                if ((x1, y1) in points and
                        (x1, y2) in points and
                        (x2, y1) in points and
                        (x2, y2) in points):

                    area = width * height
                    if area < min_area:
                        min_area = area
                    found = True

if found:
    print(min_area)
else:
    print(0)


