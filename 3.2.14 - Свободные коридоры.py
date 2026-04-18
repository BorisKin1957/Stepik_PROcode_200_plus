# Функция преобразует строку "HH:MM" в количество минут с начала суток
def to_minutes(hh_mm):
    h, m = map(int, hh_mm.split(':'))
    return h * 60 + m

# Функция преобразует количество минут обратно в строку "HH:MM"
def to_time(minutes):
    h, m = divmod(minutes, 60)
    return f"{h:02}:{m:02}"

data = []
ports = set()

for _ in range(int(input())):
    port, delta = input().split()
    tms = delta.split('-')
    start, end = to_minutes(tms[0]), to_minutes(tms[1])
    data.append((port, start, end))
    ports.add(port)

data.sort(key=lambda x: (x[0], x[1], x[2]))
ports = sorted(ports)

chart = [[data[0][0], data[0][1], data[0][2]]]

for port2, start2, end2 in data[1:]:
    port1, start1, end1 = chart[-1][0], chart[-1][1], chart[-1][2]
    if port2 == port1:
        if start2 <= end1:
            st = min(start1, start2)
            en = max(end1, end2)
            chart[-1][1] = st
            chart[-1][2] = en
        else:
            chart.append([port2, start2, end2])
    else:
        chart.append([port2, start2, end2])

for name in ports:
    tracks_name = list(filter(lambda x: x[0] == name, chart))

    n = len(tracks_name)
    result = []

    for i in range(n):
        start, end = tracks_name[i][1], tracks_name[i][2]
        if i == 0:
            result.append((0, start))
        else:
            result.append((last, start))
        last = end

    result.append((end, 1440))
    output = []
    for track in result:
        if track not in ((0,0), (1440, 1440)):
            output.append(track)

    print(name)
    if output:
        for tm in output:
            print(f'{to_time(tm[0])}-{to_time(tm[1])}')
    else:
        print('—')



