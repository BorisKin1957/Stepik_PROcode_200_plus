n = int(input())

patrols = [tuple(map(str.strip, input().split('|'))) for _ in range(n)]

# Пытаемся считать строки с приоритетами; если их нет — считаем пустыми
try:
    roles_line = input().strip()
except EOFError:
    roles_line = ''

try:
    zones_line = input().strip()
except EOFError:
    zones_line = ''

roles = list(map(str.strip, roles_line.split(','))) if roles_line else []
zones = list(map(str.strip, zones_line.split(','))) if zones_line else []

# Создаём "корзины" для группировки по приоритетам ролей
bucket_role = [[] for _ in range(len(roles) + 1)]

# Раскладываем патрули по корзинам ролей
for entry in patrols:
    name, role, zone = entry
    if role in roles:
        idx = roles.index(role)
    else:
        idx = len(roles)  # последняя корзина — для неизвестных ролей
    bucket_role[idx].append(entry)

# Формируем финальный результат
final_result = []

# Обработка сначала приоритетных ролей (с учётом зон), затем неприоритетных — без сортировки по зонам
for i, bucket in enumerate(bucket_role):
    if i < len(roles):  # Это приоритетная роль — сортируем по зонам
        bucket_zone = [[] for _ in range(len(zones) + 1)]
        for entry in bucket:
            name, role, zone = entry
            if zone in zones:
                idx = zones.index(zone)
            else:
                idx = len(zones)
            bucket_zone[idx].append(entry)
        # Склеиваем корзины зон в порядке приоритета
        for zone_bucket in bucket_zone:
            final_result.extend(zone_bucket)
    else:  # Это неприоритетная роль — НЕ сортируем по зонам, сохраняем исходный порядок
        final_result.extend(bucket)

# Выводим результат
for entry in final_result:
    print('|'.join(entry))