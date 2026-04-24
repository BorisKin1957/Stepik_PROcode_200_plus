
A, B = input().split(), input().split()

result = []

for num in A:
    if num in B:
        result.append(num)
        B.remove(num)

print(*result)
