from itertools import combinations as cb

m = int(input())

needed = {}

for i in range(m):
    s = input().split(':')
    name = s[0]
    if len(s) > 1:
        st = set(s[1].strip().split())

    else:
        st = set()

    needed[name] = st

t = float(input())

jaccard_ind = []

for pair in cb(needed.keys(), r=2):
    if needed[pair[0]] == needed[pair[1]] == set():
        jaccard_ind.append((sorted(pair), 0.0))
    else:
        a = needed[pair[0]] & needed[pair[1]]
        b = needed[pair[0]] | needed[pair[1]]
        J = round(len(a) / len(b), 2)
        if J >= t:
            jaccard_ind.append((sorted(pair), J))

result= sorted(jaccard_ind, key=lambda x: (-x[1], x[0]))

if result:
    for pair, J in result:
        print(f'{pair[0]} & {pair[1]} : {J:.2f}')