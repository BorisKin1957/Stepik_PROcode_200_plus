import math

# Функция преобразует строку "HH:MM" в количество минут с начала суток
def to_minutes(hh_mm):
    h, m = map(int, hh_mm.split(':'))
    return h * 60 + m

# Функция преобразует количество минут обратно в строку "HH:MM"
def to_time(minutes):
    h, m = divmod(minutes, 60)
    return f"{h:02}:{m:02}"


events = []

for _ in range(int(input())):
    HH_MM, h = input().split()
    time_in_minutes = to_minutes(HH_MM)
    events.append([time_in_minutes, h])

H = int(input())

portals = []

for tm, h in events:
    kz = math.floor(int(h) / H)
    low, high = kz * H, kz * H + H
    portals.append([(low, high), tm])

prt, tms = portals[0][0], portals[0][1]
result = [[prt, [tms]]]

for prt, tm in portals[1:]:
    if prt == result[-1][0]:
        result[-1][1].append(tm)
    else:
        result.append([prt, [tm]])

for prt, tms in result:
    print(f'{to_time(tms[0])}-{to_time(tms[-1])} {prt[0]}..{prt[-1]}')

