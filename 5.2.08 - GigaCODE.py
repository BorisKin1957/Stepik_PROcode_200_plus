
need = set(input().split())
c = int(input())
m = int(input())

# Словарь: кто может взять какой номер
can_offer = {num: [] for num in need}

# Список всех друзей и их квот
friends = []

for _ in range(m):
    line = input().strip()
    if ': ' in line:
        name, nums_str = line.split(': ', 1)
        available = set(nums_str.split()) & need
    else:
        name = line
        available = set()

    friends.append([name, c])  # [имя, оставшаяся квота]

    for num in available:
        can_offer[num].append(name)

# Сортируем номера по "редкости" — сначала те, у которых меньше всего друзей
sorted_nums = sorted(need, key=lambda x: len(can_offer[x]))

# Результат
assignment = []  # (номер, имя)

# Для каждого номера пытаемся назначить друга с наименьшей загрузкой
for num in sorted_nums:
    candidates = can_offer[num]
    # Сортируем кандидатов по текущей загруженности (у кого квота больше — лучше)
    candidates.sort(key=lambda name: -next(q for n, q in friends if n == name))

    for name in candidates:
        idx = next(i for i, (n, q) in enumerate(friends) if n == name)
        if friends[idx][1] > 0:  # Если у друга есть квота
            assignment.append((int(num), name))
            friends[idx][1] -= 1
            break

# Вывод
if assignment:
    assignment.sort()  # По возрастанию номера
    print(len(assignment))
    for num, name in assignment:
        print(f'{num} -> {name}')
else:
    print(0)