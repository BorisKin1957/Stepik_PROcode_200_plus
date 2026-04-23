
n = int(input())

bad = input().split()
good = input().split()

idx = {char: idx for idx, char in enumerate(good)}
count = 0

while bad != good:
    for i in range(n):
        if i == idx[bad[i]]:
            continue
        bad[i], bad[i + 1] = bad[i + 1], bad[i]
        count += 1

print(count)

