n = int(input())

if n == 0:
    print(0)
    exit()

nums = list(map(int, input().split()))

result = []

for i in range(n):
    subseq = []

    for j in range(i + 1, n):
        a, b = nums[i], nums[j]
        step = b - a
        subseq = [a, b]

        for k in range(j + 1, n):
            c = nums[k]
            if c == subseq[-1] + step:
                subseq.append(c)

        if len(subseq) > len(result):
            result = subseq[::]

print(len(result))

