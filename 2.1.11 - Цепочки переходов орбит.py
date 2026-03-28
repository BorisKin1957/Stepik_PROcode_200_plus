n, ribs = int(input()), []

for _ in range(n):
    start, end = input().split()
    ribs.append([start,end])

ribs = sorted(ribs, key=lambda x: x[0])

chains, tmp = [], ribs[0]

for i in range(n - 1):
    if ribs[i][1] == ribs[i + 1][0]:
        tmp.append(ribs[i + 1][1])
    else:
        chains.append(tmp)
        tmp = ribs[i + 1]

chains.append(tmp)

for chain in chains:
    print('->'.join(chain))