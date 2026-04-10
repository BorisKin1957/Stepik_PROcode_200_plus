

dots = [[int(num) for num in input().split()] for _ in range(int(input()))]

print(*min(dots, key=lambda x: abs(x[0]) + abs(x[1])))