s = input()
k = int(input())

n = len(s)

result = []

for i in range(n):
    for j in range(i + 1, n + 1):
        if len(set(s[i:j])) == k:
            result.append(j - i)

print(max(result) if result else 0)

