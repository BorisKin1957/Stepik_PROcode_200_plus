

map = []

for _ in range(int(input())):
    name, x, y = input().split()
    map.append([name, (int(x), int(y))])

map.sort(key=lambda x: x[0])

tracks = []


for i in range(len(map)):
    for j in range(i + 1, len(map)):
        nameA, nameB = map[i][0], map[j][0]
        xA, xB = map[i][1][0], map[j][1][0]
        yA, yB = map[i][1][1], map[j][1][1]
        d = abs(xA - xB) + abs(yA - yB)


        tracks.append([(nameA, nameB), xA, xB, yA, yB, d])

print(*map, sep='\n')
print()

print(*tracks, sep='\n')
print()

tracks.sort(key=lambda t: (t[5], t[0][0], t[0][1], t[1], t[2], t[3], t[4]))

d_min = tracks[0][5]

print(*tracks, sep='\n')

for t in tracks:
    if t[5] <= d_min:
        print(f'{t[0][0]}&{t[0][1]} @ {d_min}')



