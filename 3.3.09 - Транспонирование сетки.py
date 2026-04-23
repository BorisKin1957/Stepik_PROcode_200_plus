

n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(input().split())

result = []

for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(matrix[j][i])
    result.append(tmp)

for lst in result:
    print(*lst)

