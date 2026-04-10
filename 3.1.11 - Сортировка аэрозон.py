

dots = []

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    dots.append((x, y, z))

sorted_dots = sorted(dots, key=lambda x: (x[2], x[1], x[0]))

for dot in sorted_dots:
    print(*dot)