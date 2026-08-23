

s = input()
vol = []

n = len(s)

for i in range(n):
    w = s[i]
    for j in range(i + 1, n):
        a = w + s[j]
        if len(set(a)) == len(a):
            w += s[j]
    vol.append(w)

result = max(sorted(vol), key=lambda x: len(x))

print(result)

