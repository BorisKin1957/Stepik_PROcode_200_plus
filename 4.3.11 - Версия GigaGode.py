import sys
import bisect

# base[key] = список (st, value), отсортированный по st
base = {}

for line in sys.stdin:
    parts = line.strip().split()
    if not parts:
        continue

    if parts[0] == "GET":
        _, key, ts_str = parts
        ts = int(ts_str)

        if key not in base or not base[key]:
            print(None)
            continue

        # Получаем список времён
        all_st = [item[0] for item in base[key]]
        # Находим правую позицию: первый элемент > ts
        idx = bisect.bisect_right(all_st, ts)

        if idx == 0:
            # Нет ни одного t <= ts
            print(None)
        else:
            # Берём предыдущий — он последний с t <= ts
            print(base[key][idx - 1][1])

    elif parts[0] == "SET":
        _, key, val, ts_str = parts
        ts = int(ts_str)

        if key not in base:
            base[key] = []

        # Поищем, есть ли уже такой ts
        lst = base[key]
        all_st = [item[0] for item in lst]
        pos = bisect.bisect_left(all_st, ts)

        if pos < len(lst) and lst[pos][0] == ts:
            # Заменяем значение с тем же ts
            lst[pos] = (ts, val)
        else:
            # Вставляем новую пару
            lst.insert(pos, (ts, val))
