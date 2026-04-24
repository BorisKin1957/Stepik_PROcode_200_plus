from collections import Counter

array = list(map(int, input().split()))

D = dict(Counter(array))
num, degree = max(D.items(), key=lambda x: x[1])

if degree == 1: # Если степень равна 1, то интервал — это просто один элемент
    print(1)
    exit()

n = len(array)
intervals = []

for i in range(n):
    count = 1  # стартуем с array[i]
    for j in range(i + 1, n):
        if array[j] == array[i]:
            count += 1
        if count == degree:
            intervals.append(j - i + 1)
            break

print(min(intervals))
