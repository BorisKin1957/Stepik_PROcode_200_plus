
wanted = set(input().split())

market = {}

for _ in range(int(input())):
    try:
        name, marks = input().split(': ')
    except ValueError:
        continue
    unique_marks = set([mark for mark in marks.split()])
    market.setdefault(name, wanted & unique_marks)

result = max(market.items(), key=lambda x: len(x[1]))

print(result[0])
print(*sorted(result[1]))