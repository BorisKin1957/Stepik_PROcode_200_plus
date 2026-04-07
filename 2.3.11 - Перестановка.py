

dots = list(map(str.strip, input().split(',')))
idxes = list(map(int, input().split()))

result = ['' for i in range(len(dots))]

for dot, idx in zip(dots, idxes):
    result[idx] = dot

print(*result, sep='\n')