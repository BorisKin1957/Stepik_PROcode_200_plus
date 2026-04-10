
lst = []

for _ in range(int(input())):
    lst.append(tuple(map(int, input().split())))

print(len(lst))
print(*lst[0])
print(*lst[-1])
