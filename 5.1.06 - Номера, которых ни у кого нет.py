numbers = set(range(1, int(input()) + 1))

for _ in range(int(input())):
    lst = input().split(': ')[1]
    part = set([int(i) for i in lst.split()])
    numbers -= part

print(len(numbers))
print(*sorted(numbers))