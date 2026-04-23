
chart = [(name.split('#')[0], int(name.split('#')[1])) for name in input().split(', ')]

chart.sort(key=lambda member: member[1])

n = len(chart)
pairs = []

for i in range(n // 2):
    pairs.append((chart[i][0], chart[n - 1 - i][0]))

if n % 2:
    pairs.append(('BYE', chart[n // 2][0]))

for pair in pairs:
    print(f'{pair[0]}|{pair[1]}')
