import sys

n = int(input())
word_lst = []

while len(word_lst) < n:
    for line in sys.stdin:
        word_lst.extend(line.split())

result = []

for i in range(n):
    for j in range(n):
        if i != j:
            s = word_lst[i] + word_lst[j]
            if s == s[::-1]:
                result.append((i, j))

result.sort()

if result:
    for i, j in result:
        print(f'({i},{j})', end=' ')
else:
    print('-')