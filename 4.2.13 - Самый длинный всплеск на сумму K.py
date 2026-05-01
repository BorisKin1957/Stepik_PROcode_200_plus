

try:
    array = list(map(int, input().split()))
    n = len(array)
    k = int(input())
except EOFError:
    print(0)
    exit()

all_results = []

for i in range(n):
    for j in range(i + 1, n):
        if sum(array[i:j + 1]) == k:
            all_results.append(len(array[i:j + 1]))

print(max(all_results) if all_results else 0)