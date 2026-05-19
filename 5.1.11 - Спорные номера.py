
base = []
all = set()

for _ in range(int(input())):
    name, part = input().split(': ')
    st = set(part.split())
    base.append(st)
    all |= st

result = set()

for num in all:
    count = 0
    for st in base:
        if num in st:
            count += 1
        if count > 1:
            result.add(num)
            continue
if result:
    print(len(result))
    print(*sorted(result))
else:
    print(0)
