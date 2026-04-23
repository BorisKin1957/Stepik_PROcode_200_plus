result = []

for i in range(int(input())):
    game = input()
    p1, p2, score, set = game.split('|')
    score = score.split('-')
    if p1 == p2 or len(score) != 2 or score[0] == score[1] or set == '0':
        result.append(game)

print(*result, sep='\n') if result else print('OK')
