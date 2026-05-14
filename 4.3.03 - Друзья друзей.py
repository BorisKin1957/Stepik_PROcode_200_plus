


f = int(input())

guys = {}

for i in range(f):
    name_1, name_2 = input().split()
    guys[name_1] = guys.get(name_1, set())
    guys[name_1].add(name_2)
    guys[name_2] = guys.get(name_2, set())
    guys[name_2].add(name_1)

#print(guys)

b = int(input())

foes = {}
for i in range(b):
    name_1, name_2 = input().split(' ! ')
    foes[name_1] = foes.get(name_1, set())
    foes[name_1].add(name_2)
    foes[name_2] = foes.get(name_2, set())
    foes[name_2].add(name_1)

#print(foes)

s = input().split()

user, k = s[0], int(s[1])

result = {}
base = guys.get(user, set())

for name in base:
    if guys.get(name):
        for guy in guys.get(name):
            if guy not in base and not foes.get(guy) and guy != user:
                result[guy] = result.get(guy, 0) + 1

if result:
    result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    if len(result) > k:
        result = result[:k]
    for guy, score in result:
        print(f'{guy}:{score}')
else:
    print('-')






