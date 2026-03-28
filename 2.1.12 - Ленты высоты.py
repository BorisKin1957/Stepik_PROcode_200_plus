'''
Считай k, затем k строк:

HH:MM z


(время неубывающее; в одну минуту может быть несколько точек), затем целое H (H > 0).

Для каждой точки вычисли её коридор:

kz = floor(z / H)
low = kz * H
high = low + H          # верхняя граница не входит


Сверни последовательность в блоки подряд идущих одинаковых коридоров.
Для каждого блока выведи:

HH:MM_start-HH:MM_end low..high


где HH:MM_start --> время первой точки блока, HH:MM_end --> время последней
точки блока (если в блоке одна точка, то времена совпадают). Порядок блоков -->
по времени.

Уточнения:

Деление --> настоящий пол floor. Для языков с усечением к нулю при z < 0
используйте безопасную формулу floorDiv.

Если несколько точек с одинаковым HH:MM попали в разные коридоры,
это разные соседние блоки с одинаковым временем начала/конца.

🧪 Пример 1 — ввод

5
08:00 12
08:05 15
08:06 21
08:07 25
08:12 8
10


🧪 Пример 1 — вывод

08:00-08:05 10..20
08:06-08:07 20..30
08:12-08:12 0..10
'''


data = []
k = int(input())

for _ in range(k):
    line = input().strip()
    time_str, z_str = line.split()
    h, m = map(int, time_str.split(':'))
    z = int(z_str)
    data.append((h * 60 + m, time_str, z))  # сохраняем минуты с начала суток, строку времени и z

H = int(input())

blocks = []
current_block = None

for minutes, time_str, z in data:
    kz = z // H
    low = kz * H
    high = low + H

    # Ключ блока — диапазон коридора
    corridor_key = (low, high)

    if current_block is None or current_block['corridor'] != corridor_key:
        # Завершаем предыдущий блок
        if current_block is not None:
            blocks.append(current_block)
        # Начинаем новый блок
        current_block = {
            'start_time': time_str,
            'end_time': time_str,
            'corridor': corridor_key,
            'low': low,
            'high': high
        }
    else:
        # Продолжаем текущий блок
        current_block['end_time'] = time_str

# Добавляем последний блок
if current_block is not None:
    blocks.append(current_block)

# Выводим результат
for block in blocks:
    print(f"{block['start_time']}-{block['end_time']} {block['low']}..{block['high']}")

