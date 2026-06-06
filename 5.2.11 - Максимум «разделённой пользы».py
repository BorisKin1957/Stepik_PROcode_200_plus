from itertools import combinations as cb

def get_vol(s: str) -> set:
    lst = s.split(': ')
    if len(lst) > 1:
        return set(lst[1].split())
    return set()

n = int(input())

offers, needed = {}, {}

for _ in range(n):
    name = input()
    offers[name] = get_vol(input())
    needed[name] = get_vol(input())

pairs = list(cb(offers, r=2))
names, numbers, exchanges = set(), set(), []

for pair in pairs:
    name1, name2 = pair
    x = offers[name1] & needed[name2]
    y = offers[name2] & needed[name1]

    if (len(x) == len(y) == 1
            and x != y
            and not names & {name1, name2}
            and not numbers & (x | y)):
        exchanges.append([(name1, name2), (*x, *y)])
        names |= {name1, name2}
        numbers |= x | y

if exchanges:
    for exc in exchanges:
        print(f'{exc[0][0]} <-> {exc[0][1]} : {exc[1][0]}|{exc[1][1]}')

