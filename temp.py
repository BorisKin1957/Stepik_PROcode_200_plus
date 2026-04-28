array = list(map(int, input().split()))
k = int(input())

n = len(array)
variants = []


for i in range(n):
    tmp = []
    for j in range(i, n):
        if sum(tmp) == k:
            variants.append(tmp)
            tmp = []
            break
        else:
            if sum(tmp) > k:
                break
            else:
                tmp.append(array[j])

    if sum(tmp) == k:
        variants.append(tmp)

print(len(variants))