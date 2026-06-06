from itertools import combinations as cb
m = int(input())

all = {}
all_need = set()

for i in range(m):
    s = input().split(': ')
    name = s[0]
    if len(s) > 1:
        st = set(s[1].split())
        all_need |= st
    else:
        st = set()
    all[name] = st

all_result = []

for i in range(1, m + 1):
    for vol in cb(all_need, r=i):
        flag = True
        for need in all.values():
            if not set(vol) & need:
                flag = False
                break
        if flag:
            all_result.append(vol)

if all_result:
    min_len = len(min(all_result, key=len))
else:
    print('Пусто')
    exit()

result = list(filter(lambda x: len(x) == min_len, all_result))
result = sorted([sorted([int(i) for i in s]) for s in result])

for vol in result:
    print(*vol)
