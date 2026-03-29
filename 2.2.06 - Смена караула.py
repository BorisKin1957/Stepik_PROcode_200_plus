
tags = list(map(str.strip, input().split()))
k = int(input())

n = len(tags)
k = k % n

result = tags[n - k:] + tags[:n - k]

print(*result)