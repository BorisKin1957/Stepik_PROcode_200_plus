
from itertools import combinations as cb

numbers = map(int, input().split())
k = int(input())

pairs = set(cb(numbers, r=2))

result = 0

for pair in pairs:
    if abs(pair[0] - pair[1]) == k:
        result += 1

print(result)