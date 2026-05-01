try:
    array = list(map(int, input().split()))
    n = len(array)
    d = int(input())
except EOFError:
    print(0)
    exit()

if d > 0:
    array.sort()
else:
    array.sort(reverse=True)

results = []
max_result = 0

for i in range(n):
    tmp = [array[i]]
    for j in range(i + 1, n):
        a, b = tmp[-1], array[j]
        if b - a == d:
            tmp.append(array[j])
    if len(tmp) > max_result:
        max_result = len(tmp)
        results.append(tmp)

print(len(max(results, key=len)) if results else 0)


