

data = []

for _ in range(int(input())):
    p1, p2, score, round = input().split('|')
    data.append([p1, p2, round])

name = input()

opponents = []

for item in data:
    if name in item:
        if '—BYE—' in item:
            continue
        slice, round = item[:2], int(item[-1])
        slice.remove(name)
        opponents.append((slice[0], round))

opponents.sort(key=lambda x: x[1])

result = []

for tpl in opponents:
    result.append(tpl[0])

print(f'({name}, ({', '.join(result)}))')




