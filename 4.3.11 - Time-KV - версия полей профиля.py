import sys, bisect

base = {}
all_ts = {}

for line in sys.stdin:
    s = line.strip().split()
    if len(s) == 3:
        key, ts = s[1], int(s[-1])

        if key in base:
            idx = bisect.bisect_left(all_ts[key], ts)

            if ts < min(all_ts[key]):
                print(None)
                continue

            if len(all_ts[key]) == 1:
                result = base[key][0][-1]

            else:
                try:
                    if ts >= base[key][idx][0]:
                        result = base[key][idx][-1]
                    else:
                        result = base[key][idx - 1][-1]
                except IndexError:
                    result = base[key][idx - 1][-1]

            print(result)
        else:
            print(None)

    else:
        key, val, ts = s[1], s[2], int(s[3])

        if key in all_ts and ts in all_ts[key]:
            ind_ts = all_ts[key].index(ts)
            base[key].pop(ind_ts)

        base[key] = base.get(key, []) + [(ts, val)]
        base[key].sort(key=lambda x: x[0])

        all_ts[key] = [int(i[0]) for i in base[key]]
