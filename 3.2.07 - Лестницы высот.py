from math import floor

labels = []

for _ in range(int(input())):
    l = input().split()
    name, _, _, z = l[0], l[1], l[2], int(l[3])
    labels.append((name, z))

H = int(input())

groups = []

for name, z in labels:
    k = floor(z / H)
    low, high = k * H, (k + 1) * H
    groups.append((name, (low, high)))

groups.sort(key=lambda x: (x[1][0], x[1][1], x[0]))

result = {}

for name, (low, high) in groups:
    result[(low, high)] = result.get((low, high), '') + ' ' + name

for label, names in result.items():
    print(f'{label[0]}..{label[1]}')
    print(names.strip())
