

numbers = []

for _ in range(int(input())):
    lst = input().split(': ')[1]
    numbers.append(set([int(i) for i in lst.split()]))

all = set()

for part in numbers:
    all |= part

result = set()

for i in range(len(numbers)):
    unique = set()
    unique |= all
    st = set()
    other = numbers[:]
    other.pop(i)
    for part in other:
        st |= part
    unique -= st
    result |= unique

print(len(result))
print(*sorted(result))



