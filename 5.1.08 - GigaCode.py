

needed = set(map(int, input().split())) if input().strip() else set()

M = int(input())
friends = {}

for _ in range(M):
    line = input().strip()
    if ':' not in line:
        continue
    name, nums_part = line.split(':', 1)
    name = name.strip()
    nums = set(map(int, nums_part.strip().split())) if nums_part.strip() else set()
    friends[name] = nums

if M < 2:
    print("Нет пары")
    print()
else:
    # Считаем покрытие для каждого
    cover = {}
    for name, have in friends.items():
        cover[name] = len(have & needed)

    # Перебираем все пары
    best_score = -1
    best_pair = None  # (name1, name2) с name1 < name2
    best_numbers = set()

    names = list(friends.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            ca, cb = cover[a], cover[b]
            score = ca + cb

            # Определяем порядок имён
            if a <= b:
                pair = (a, b)
            else:
                pair = (b, a)

            # Сравниваем
            if score > best_score:
                best_score = score
                best_pair = pair
                # Считаем объединение покрытий
                nums_a = friends[a] & needed
                nums_b = friends[b] & needed
                best_numbers = nums_a | nums_b
            elif score == best_score:
                # Лексикографически минимальная пара
                if pair < best_pair:
                    best_pair = pair
                    nums_a = friends[a] & needed
                    nums_b = friends[b] & needed
                    best_numbers = nums_a | nums_b

    if best_pair:
        print(f"{best_pair[0]} & {best_pair[1]}")
        print(*sorted(best_numbers))
    else:
        print("Нет пары")
        print()