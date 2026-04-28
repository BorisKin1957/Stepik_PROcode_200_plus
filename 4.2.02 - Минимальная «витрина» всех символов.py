

try:
    s, t = list(input()), list(input())
except EOFError:
    exit()

slices = []
tmp = []
n = len(s)
t_ = t[::]

for i in range(n):
    if t_:
        if s[i] in t_:
            t_.remove(s[i])
            tmp.append(s[i])
        else:
            if tmp:
                tmp.append(s[i])
    else:
        slices.append(tmp)
        tmp = []
        t_ = t[::]

slices.append(tmp)

result = min(slices, key=len)

if len(result) < len(t):
    print('Пусто')
else:
    print(''.join(result))