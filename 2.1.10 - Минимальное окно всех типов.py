'''
Считай n, затем n строк неубывающего времени:

HH:MM type

где type --> строка без пробелов; в одну минуту может быть несколько событий.

Пусть множество типов --> все различные type из входа. Найди минимальный по
длительности в минутах непрерывный отрезок входной последовательности [L..R]
(по индексам), содержащий хотя бы по одному событию каждого типа.

Выведи одну строку:

Ltime-Rtime

где Ltime --> время на позиции L, Rtime --> время на позиции R (формат HH:MM).
Если подходящего окна нет (например, n = 0), выведи Пусто.

Уточнения:
- Длительность = minutes(Rtime) - minutes(Ltime); допустима нулевая длина.
- При равной длительности приоритет:
  1. минимальный Ltime
  2. минимальный Rtime
  3. минимальный индекс L
'''

from collections import defaultdict

def time_to_minutes(time_str):
    """Переводит строку 'HH:MM' в количество минут с начала суток."""
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def minutes_to_time(minutes):
    """Переводит количество минут обратно в формат 'HH:MM'."""
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"

# Чтение входа
n = int(input().strip())
if n == 0:
    print("Пусто")
    exit()

events = []
types = set()

for _ in range(n):
    line = input().strip()
    time_str, event_type = line.split(' ', 1)
    events.append((time_str, event_type))
    types.add(event_type)

total_types = len(types)

# Если нет событий — невозможно покрыть все типы
if total_types == 0:
    print("Пусто")
    exit()

# Используем метод скользящего окна (two pointers)
left = 0
type_count = defaultdict(int)  # Сколько раз каждый тип встречается в текущем окне
covered_types = 0  # Сколько различных типов уже покрыто окном
best_window = None  # Будет хранить (duration, Ltime_minutes, Rtime_minutes, L_index)

for right in range(n):
    # Добавляем событие справа
    _, typ = events[right]
    if type_count[typ] == 0:
        covered_types += 1
    type_count[typ] += 1

    # Пытаемся сжать окно слева, пока условие всё ещё выполняется
    while covered_types == total_types:
        # Текущее окно [left, right] содержит все типы
        Ltime_str, _ = events[left]
        Rtime_str, _ = events[right]
        Ltime_min = time_to_minutes(Ltime_str)
        Rtime_min = time_to_minutes(Rtime_str)
        duration = Rtime_min - Ltime_min

        # Ключ для сравнения: (длительность, начало, конец, индекс left)
        candidate = (duration, Ltime_min, Rtime_min, left)

        if best_window is None or candidate < best_window:
            best_window = candidate

        # Убираем левый элемент и двигаем left
        _, left_type = events[left]
        type_count[left_type] -= 1
        if type_count[left_type] == 0:
            covered_types -= 1
        left += 1

# Вывод результата
if best_window is None:
    print("Пусто")
else:
    _, Ltime_min, Rtime_min, _ = best_window
    Ltime_str = minutes_to_time(Ltime_min)
    Rtime_str = minutes_to_time(Rtime_min)
    print(f"{Ltime_str}-{Rtime_str}")