


s = input()
n = len(s)

if n <= 10:
    exit()

st = set()
k = 0
result = set()

for i in range(n - 9):
    pat = s[i:i + 10]
    st |= {pat}
    if i + 1 != len(st) + k:

        result |= {pat}
        k += 1

print('\n'.join(sorted(result)))




