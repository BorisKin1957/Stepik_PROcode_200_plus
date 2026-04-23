

result = {}
members = set()
flag = True

for _ in range(int(input())):
    p1, p2 = input().split()
    result[p1] = result.get(p1, 0) + 1
    members.add(p1)
    members.add(p2)

if not members:
    flag = False

for name, count in result.items():
    if count == len(members) - 1:
        winner = name
        break
    else:
        flag = False

print(winner if flag else 'НЕТ')