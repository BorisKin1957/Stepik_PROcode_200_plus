
def to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def to_time(minutes):
    h, m = divmod(minutes, 60)
    return f"{h:02}:{m:02}"

events = []

for i in range(2):
    for _ in range(int(input())):
        src = 'A' if i == 0 else 'B'
        HM, label, value = input().split()
        mm = to_minutes(HM)
        value = int(value)
        events.append((mm, src, label, value))

events.sort(key=lambda x: (x[0], x[1]))

for mm, src, label, value in events:
    print(f'{to_time(mm)} {src} {label} {value}')