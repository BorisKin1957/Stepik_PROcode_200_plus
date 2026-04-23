'''
Считай n, затем n строк матчей p1|p2|s1-s2|round.

Для каждого игрока посчитай:

    wins --> число побед,
    losses -> число поражений,
    opp_sum --> сумма очков, набранных соперниками против него (то есть сумма очков
    оппонентов именно в матчах с этим игроком).

Отсортируй записи по ключу (-wins, -opp_sum, name). Выведи строки name|wins|losses|opp_sum.
🧪 Примеры ввода/вывода

Пример 1

4
Ари|Дэн|10-7|1
Ива|Кай|9-11|1
Ари|Кай|8-11|2
Дэн|Ива|7-6|2


Кай|2|0|17
Ари|1|1|18
Дэн|1|1|16
Ива|0|2|18
'''

games = []
names = set()

for i in range(int(input())):
    game = input()
    p1, p2, score, _ = game.split('|')
    s1, s2 = score.split('-')
    games.append({p1: int(s1), p2: int(s2)})
    names.add(p1)
    names.add(p2)

#print(games)

tables = {}

for name in names:
    tables[name] = tables.get(name, [0, 0, 0])

#print(tables)
print()
maded_games = []

for name in names:
    for game in games:
        if name in game and game not in maded_games:
            lst = list(game.keys())
            lst.remove(name)
            rival = lst[0]
            if game[name] > game[rival]:
                tables[name][0] += 1
                tables[rival][1] += 1

            elif game[name] < game[rival]:
                tables[rival][0] += 1
                tables[name][1] += 1

            tables[name][2] += game[rival]
            tables[rival][2] += game[name]
            maded_games.append(game)

tables = sorted(tables.items(), key=lambda x: (-x[1][0], -x[1][2], x[1][1]))

for line in tables:
    print(f'{line[0]}|{line[1][0]}|{line[1][1]}|{line[1][2]}')







