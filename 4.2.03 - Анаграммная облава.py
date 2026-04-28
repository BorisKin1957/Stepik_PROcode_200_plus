

try:
    s, t = list(input()), list(input())
except EOFError:
    exit()

tmp, slices = [], []

n, m = len(s), len(t)

if m > n:
    exit()

t_ = t[::]

for i in range(n):
    if s[i] in t_:
        tmp = [i]
        t_.remove(s[i])
        count = 0
        for j in range(i + 1, n):
            if len(tmp) != m:
                if s[j] in t_:
                    tmp.append(j)
                    t_.remove(s[j])
                else:
                    t_ = t[::]
                    break
            else:
                slices.append(tmp)
                t_ = t[::]
                break
    else:
        continue

if tmp and len(tmp) == m:
    slices.append(tmp)

if slices:
    result = []
    for idx in slices:
        result.append(idx[0])

    print(*result)