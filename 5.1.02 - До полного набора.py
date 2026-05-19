

all = set(range(1, int(input()) + 1))
st = set(map(int, input().split()))

all -= st
result = sorted(all)

print(len(result))
print(*result)