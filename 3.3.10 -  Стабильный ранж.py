
data = [tuple(input().split('|')) for _ in range(int(input()))]

data.sort(key=lambda x: (-int(x[1]), -int(x[2]), x[0]))

for line in data:
    print('|'.join(line))