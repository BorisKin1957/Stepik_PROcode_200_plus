
numbers = list(map(int, input().split()))
summ = int(input())

n = len(numbers)
result = []

# for i in range(n):
#     for j in range(i + 1, n):
#         if numbers[i] + numbers[j] == summ:
#             result.append((i, j))

result = [(i, j) for i in range(n) for j in range(i + 1, n) if numbers[i] + numbers[j] == summ]

print(*result[-1]) if result else print(None)

