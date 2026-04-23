

result = {}

for i in range(int(input())):
    names = tuple(sorted(input().split('|')[:2]))
    result[names] = result.get(names, 0) + 1

for names, count in result.items():
    if count > 1:
        print(f'{names[0]}&{names[1]}')