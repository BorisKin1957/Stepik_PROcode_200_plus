

n = int(input())
games = []
names = set()

for _ in range(n):
    line = input().strip()
    p1, p2, score, round_num = line.split('|')
    s1, s2 = map(int, score.split('-'))
    games.append((p1, p2, s1, s2))
    names.add(p1)
    names.add(p2)

# Словарь: имя -> [wins, losses, opp_sum]
table = {name: [0, 0, 0] for name in names}

# Обрабатываем каждый матч
for p1, p2, s1, s2 in games:
    # Обновляем статистику по победам/поражениям
    if s1 > s2:
        table[p1][0] += 1  # win for p1
        table[p2][1] += 1  # loss for p2
    elif s2 > s1:
        table[p2][0] += 1  # win for p2
        table[p1][1] += 1  # loss for p1

    # Добавляем очки соперника к opp_sum
    table[p1][2] += s2  # p2's score in this match
    table[p2][2] += s1  # p1's score in this match

# Сортируем по: (-wins, -opp_sum, name)
sorted_players = sorted(table.items(), key=lambda x: (-x[1][0], -x[1][2], x[0]))

# Выводим результат
for name, (wins, losses, opp_sum) in sorted_players:
    print(f"{name}|{wins}|{losses}|{opp_sum}")