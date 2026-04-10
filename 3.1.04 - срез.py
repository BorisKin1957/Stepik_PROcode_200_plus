

names = tuple(input().split())
l, r = map(int, input().split())

print(*names[l:r + 1])