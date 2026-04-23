

winners = []

for i in range(int(input())):
    p1, p2, score, set = input().split('|')
    s1, s2 = score.split('-')
    game = [(p2, int(s2)), (p1, int(s1))]
    game.sort(key=lambda x: -x[1])
    winners.append(game[0][0])

n = len(winners)
pairs = []

for i in range(n // 2):
    pairs.append((winners[i], winners[n - 1 - i]))

if n % 2:
    pairs.append(('BYE', winners[n // 2]))

for pair in pairs:
    print(f'{pair[0]}|{pair[1]}')