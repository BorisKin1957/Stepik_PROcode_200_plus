def get_tangent(x, y):
    if x == 0:
        return 0
    return round(y / x, 3)

def get_new_tg(x, y, tg):
    x_new = x / 2
    y_ = tg * x_new
    y_new = y - y_
    return get_tangent(x_new, y_new)

points = [tuple(map(int, input().split())) for _ in range(int(input()))]
points.sort(key=lambda x: -x[0])

n = len(points)
lines = []
dup = 0
slopes = []

for i in range(n):
    x1, y1 = points[i]
    tg_1 = get_tangent(x1, y1)
    slope = set()

    for j in range(i + 1, n):
        if points[j] == points[i]:
            dup += 1
        x2, y2 = points[j]
        tg_2 = get_tangent(x2, y2)

        for k in range(j + 1, n):
            if points[k] == points[j] or points[k] == points[i]:
                dup += 1
            x3, y3 = points[k]

            if x1 == x2 == x3 or y1 == y2 == y3:
                slope.add(i)
                slope.add(j)
                slope.add(k)

            else:
                if x3 != 0:
                    tg_3 = get_tangent(x3, y3)
                else:
                    x3_new = x1 / 2
                    y3_ = tg_1 * x3_new
                    y3_new = y1 - y3_
                    tg_3 = get_new_tg(x1, y1, tg_1)

                if tg_1 == tg_2 and tg_1 == tg_3:
                    slope.add(i)
                    slope.add(j)
                    slope.add(k)

    slopes.append(slope)

print(len(max(slopes, key=len)))

    

