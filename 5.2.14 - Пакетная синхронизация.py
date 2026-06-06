data = set(input().split())

for _ in range(int(input())):
    s = input().split(':')
    if s[0] == 'ADD':
        data |= set(s[1].strip().split())
    elif s[0] == 'REMOVE':
        data -= set(s[1].strip().split())
    else:
        data ^= set(s[1].strip().split())
if data:
    print(*sorted(data))

