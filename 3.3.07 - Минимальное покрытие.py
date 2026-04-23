'''
8
10|A
12|B
13|A
15|C
19|B
21|C
22|A
30|B


'''

events = []
types = set()

for _ in range(int(input())):
    t, e = input().split('|')
    types.add(e)
    events.append((t, e))

if not events or len(types) == 1:
    print('Пусто')
    exit()

variants = []

for i in range(len(events) - len(types) + 1):
    tmp, variant = set(events[i][1]), [events[i]]
    for j in range(i + 1, len(events)):
        if tmp != types:
            variant.append(events[j])
            tmp.add(events[j][1])
        else:
            variants.append(variant)
variants.append(variant)
delta = []

for v in variants:
    delta.append((v[0][0], v[-1][0]))

result = min(delta, key=lambda x: int(x[1]) - int(x[0]))


print(f'{result[0]}-{result[1]}')








