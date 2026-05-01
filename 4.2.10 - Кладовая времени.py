def get_max_key(dct: dict, num: int) -> str:
    lst = []
    for k in dct.keys():
        if k <= num:
            lst.append(k)
    if lst:
        return dct[max(lst)]
    return None


D = {}
n = int(input())

if not n:
    exit()

for _ in range(n):
    L = input().split()
    if L[0] == 'SET':
        D[int(L[3])] = L[2]
    if L[0] == 'GET':
        print(get_max_key(D, int(L[2])))
