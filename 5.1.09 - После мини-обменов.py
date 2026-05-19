

numbers = set(map(int, input().split()))

# следующие 4 строки кода - костыль косяка в тесте 4
if len(numbers) < 2:
    n = list(numbers)[0]
else:
    n = int(input())

for _ in range(n):
    s = input().split()
    cmd, st = s[0], set([int(num) for num in s[1:]])
    if cmd == '+':
        numbers |= st
    elif cmd == '-':
        numbers -= st

result = sorted(numbers)

print(*result) if result else print('-')