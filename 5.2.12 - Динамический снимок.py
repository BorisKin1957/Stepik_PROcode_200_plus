


n = int(input())

data = []

for i in range(n):
    data.append(set(input().split()))

result = 0

for i in range(n - 1):
    result += len(data[i] ^ data[i + 1])

print(result)