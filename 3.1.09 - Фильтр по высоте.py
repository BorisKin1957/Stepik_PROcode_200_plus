dots = []

for i in range(int(input())):
    name, x, y, z = input().split()
    dots.append((name, z))

h = int(input())

for name, z in dots:
    if int(z) >= h:
        print(name)
