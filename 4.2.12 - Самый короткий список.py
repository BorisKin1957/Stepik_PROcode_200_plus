from collections import Counter

def get_true(lst, sample):
    dct = dict(Counter(lst))
    for num in sample:
        if num not in dct:
            return False
        if num in dct and dct[num] < sample[num]:
            return False
    return True


try:
    array = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    n = len(array)
    k = len(lst)
except EOFError:
    print('Пусто')
    exit()

result = []

dct = dict(Counter(lst))

for i in range(n):
    for j in range(i, n - k):
        tmp = array[i:j + k]
        if get_true(tmp, dct):
            result.append((i + 1, j + k))
            break

if result:
    result = min(result, key=lambda x: (x[1] - x[0], x[0]))
    print(*result)
else:
    print('Пусто')


