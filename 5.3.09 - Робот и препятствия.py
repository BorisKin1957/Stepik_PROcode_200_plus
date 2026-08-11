n = int(input().strip())
commands = list(map(int, input().strip().split()))
m = int(input().strip())

# Считываем препятствия
obstacles = set()
for _ in range(m):
    x, y = map(int, input().strip().split())
    obstacles.add((x, y))

# Направления: север, восток, юг, запад
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0  # Начинаем с севера

x, y = 0, 0
max_dist_sq = 0

for cmd in commands:
    if cmd == -1:  # Поворот направо
        dir_idx = (dir_idx + 1) % 4
    elif cmd == -2:  # Поворот налево
        dir_idx = (dir_idx - 1) % 4
    else:  # Движение вперёд на cmd шагов
        dx, dy = directions[dir_idx]
        for _ in range(cmd):
            # Проверяем, есть ли препятствие в следующей точке
            next_x, next_y = x + dx, y + dy
            if (next_x, next_y) in obstacles:
                break  # Останавливаемся перед препятствием
            x, y = next_x, next_y
            # Обновляем максимум
            dist_sq = x * x + y * y
            if dist_sq > max_dist_sq:
                max_dist_sq = dist_sq

print(max_dist_sq)
