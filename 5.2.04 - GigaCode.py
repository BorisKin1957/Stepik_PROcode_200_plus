
need = set(input().split())
D = int(input())

# Список множеств по дням (по порядку)
offers = []
for _ in range(D):
    line = input().strip()
    if ': ' in line:
        nums = line.split(': ')[1].split()
    else:
        nums = []
    offers.append(set(nums))

# Поиск минимального непрерывного интервала [L, R] (1-индексация)
l = 0
current = set()
best = None
min_length = float('inf')

for r in range(D):
    # Добавляем день r
    current |= offers[r]

    # Пытаемся сжать окно с левого края
    while l <= r and current >= need:  # current содержит need
        length = r - l + 1
        if length < min_length or (length == min_length and (best is None or l < best[0])):
            min_length = length
            best = (l, r)
        # Убираем левый день
        current -= offers[l]
        l += 1
    # После выхода из while условие current >= need уже не выполняется
    # Но мы уже сохранили best при выполнении условия

if best is not None:
    L, R = best
    print(L + 1, R + 1)  # 1-индексация
else:
    print('Пусто')