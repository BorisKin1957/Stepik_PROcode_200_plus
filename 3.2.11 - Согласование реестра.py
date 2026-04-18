REG = []

for _ in range(int(input())):
    name, buoy = input().split()
    REG.append((name, buoy))

AIR = []

for _ in range(int(input())):
    name, buoy = input().split()
    AIR.append((name, buoy))

MISSING = set(REG) - set(AIR)

EXTRA = set(AIR) - set(REG)

print('MISSING')
for item in sorted(MISSING):
    print(*item)

print('EXTRA')
for item in sorted(EXTRA):
    print(*item)