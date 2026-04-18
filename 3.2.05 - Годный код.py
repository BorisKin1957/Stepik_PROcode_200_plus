
import sys

def parse_line(line):
    parts = line.strip().split()
    port = parts[0]
    time_range = parts[1]
    start_str, end_str = time_range.split('-')

    def to_minutes(time_str):
        h, m = map(int, time_str.split(':'))
        return h * 60 + m

    start = to_minutes(start_str)
    end = to_minutes(end_str)
    return port, start, end

# Чтение первой группы (смена A)
a = int(sys.stdin.readline().strip())
shift_a = []
for _ in range(a):
    line = sys.stdin.readline().strip()
    shift_a.append(parse_line(line))

# Чтение второй группы (смена B)
b = int(sys.stdin.readline().strip())
shift_b = []
for _ in range(b):
    line = sys.stdin.readline().strip()
    shift_b.append(parse_line(line))

# Объединяем все интервалы
all_intervals = shift_a + shift_b

# Группируем по порту
port_intervals = {}
for port, start, end in all_intervals:
    if port not in port_intervals:
        port_intervals[port] = []
    port_intervals[port].append((start, end))

# Обрабатываем каждый порт
result = []
for port in sorted(port_intervals.keys()):
    intervals = sorted(port_intervals[port])  # сортируем по началу
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:  # можно склеить
            prev_start, prev_end = merged.pop()
            merged.append((prev_start, max(prev_end, end)))
        else:
            merged.append((start, end))
    port_intervals[port] = merged
    result.append((port, merged))

# Выводим результат
for port in sorted(port_intervals.keys()):
    print(port)
    for start, end in port_intervals[port]:
        def to_time_str(minutes):
            h, m = divmod(minutes, 60)
            return f"{h:02}:{m:02}"
        print(f"{to_time_str(start)}-{to_time_str(end)}")