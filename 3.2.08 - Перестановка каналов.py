

n, m = map(int, input().split())

M = tuple([tuple([x for x in input().split()]) for i in range(n)])
L = [[''] * n for i in range(m)]

for i in range(n):
    for j in range(m):
        L[j][i] = M[i][j]

M = tuple([tuple(lst) for lst in L])

for tpl in M:
    print(*tpl)



