tracks_old = []

for _ in range(int(input())):
    lst = input().split()
    lane, start, end = lst[0], int(lst[1]), int(lst[2])
    tracks_old.append([lane, (start, end)])

D = {}

for _ in range(int(input())):
    old, new = input().split()
    D[old] = new

tracks_new = []

for lane, track in tracks_old:
    tracks_new.append([D[lane], track])

tracks_new.sort(key=lambda t: (t[0], t[1][0], t[1][1]))

for lane, track in tracks_new:
    print(f'{lane} {track[0]}-{track[1]}')




