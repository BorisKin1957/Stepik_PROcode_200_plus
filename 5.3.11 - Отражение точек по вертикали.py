
import sys
from collections import defaultdict


data = sys.stdin.read().strip().split()
if not data:
    exit()
n = int(data[0])
points = []
idx = 1
for _ in range(n):
    x = int(data[idx])
    y = int(data[idx + 1])
    points.append((x, y))
    idx += 2

if n <= 1:
    print("YES")
    exit()

groups = defaultdict(list)
for x, y in points:
    groups[y].append(x)

common_sum = None  # 2 * k, где k – координата оси симметрии

for y, xs in groups.items():
    xs.sort()
    m = len(xs)
    target = xs[0] + xs[-1]  # 2*k для этой группы

    # Проверяем симметричность списка xs относительно target/2
    ok = True
    for i in range(m // 2 + 1):
        if xs[i] + xs[m - 1 - i] != target:
            ok = False
            break

    if not ok:
        print("NO")
        exit()

    if common_sum is None:
        common_sum = target
    elif common_sum != target:
        print("NO")
        exit()

print("YES")


