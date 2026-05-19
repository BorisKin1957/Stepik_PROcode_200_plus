
needed = set(map(int, input().split()))

exchange_base = {}

n = int(input())

if n < 2:
    print('Нет пары')
    exit()

for _ in range(n):
    name, part = input().split(': ')
    digs = set([int(num) for num in part.split()])
    exchange_base[name] = digs

variants = {}

for key, value in exchange_base.items():
    value &= needed
    variants[key] = value

all = sorted(variants.items(), key=lambda x: (-len(x[1]), x[0]))

sponsors = sorted(all[:2])

names = f'{sponsors[0][0]} & {sponsors[1][0]}'
result = sponsors[0][1] | sponsors[1][1]

print(names)
print(*result)









