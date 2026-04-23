def is_crossing(s1, e1, s2, e2):
    return max(s1, s2) < min(e1, e2)

def get_result(item, data, flag):
    res = []
    if flag:
        cross = list(filter(lambda x: x[1] == item, data))
    else:
        cross = list(filter(lambda x: x[-1] == item, data))
    n = len(cross)
    for i in range(n):
        for j in range(i + 1, n):
            num1, _, start1, end1, ref = cross[i]
            num2, _, start2, end2, ref2 = cross[j]
            if is_crossing(start1, end1, start2, end2):
                res.append((num1, num2))
    return res



n = int(input())
games = []

forums, arbitr = set(), set()

for i in range(n):
    ref = None
    line = input().split('|')
    if len(line) == 5:
        p1, p2, _, arena, delta = line
    else:
        p1, p2, _, arena, delta, ref = line
    forums.add(arena)
    arbitr.add(ref)
    start, end = delta.split('-')
    games.append((i + 1, arena, int(start), int(end), ref))

matches = []

for arena in forums:
    result = get_result(arena, games, True)
    if result:
        matches.append(*result)
if ref:
    for ref in arbitr:
        result = get_result(ref, games, False)
        if result:
            matches.append(*result)
if matches:
    for match in matches:
        print(f'MATCH#{match[0]} & MATCH#{match[1]}')
else:
    print('OK')
                



