
n, m = map(int, input().split())

# Проверка на некорректные размеры
if n <= 0 or m <= 0:
    print('')
else:
    matrix = [input().split() for _ in range(n)]
    flatten = []
    while matrix:
        flatten += matrix.pop(0)
        matrix = [*zip(*matrix)][::-1]

print(*flatten)