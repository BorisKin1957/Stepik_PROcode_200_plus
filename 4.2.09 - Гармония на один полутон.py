from collections import Counter

try:
    array = [int(num) for num in input().split()]
    min_num, max_num = min(array), max(array)
except (EOFError, ValueError):
    print(0)
    exit()

num_count = dict(Counter(array))
result = []

for i in range(min_num, max_num):
    if i in num_count and i + 1 in num_count:
        result.append(num_count[i] + num_count[i + 1])

print(max(result) if result else 0)

