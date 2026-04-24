from collections import Counter

note = Counter(input())
stock = Counter(input())

flag = True

for k, v in note.items():
    vol = stock.get(k, 0)
    if vol == 0 or vol < v:
        flag = False
        break


print('YES' if flag else 'NO')