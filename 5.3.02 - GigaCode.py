
'''
Задание
В замке есть 4-значный кодовый диск.

В первой строке вводится число m -- сколько комбинаций заблокировано.

Затем идут m строк, каждая строка содержит по 4 цифры -- это запрещённые коды.

В последней строке записан код target, к которому нужно добраться.

Стартовая комбинация всегда "0000".

За один шаг можно прокрутить одну цифру вперёд или назад на 1
(с учётом цикличности: после 9 идёт 0, а перед 0 идёт 9).

Нужно найти минимальное количество шагов, чтобы из "0000" получить код target,
не заходя в запрещённые комбинации.
Если это невозможно, выведи -1.

🧪 Примеры ввода/вывода
Тестовые данные
№ Теста
Входные данные
Выходные данные
1

6
0201
0101
0102
1212
2002
9999
0202

6
'''

from collections import deque

def open_lock(m, forbidden_codes, target):
    # Преобразуем запрещённые коды в множество для быстрого поиска
    forbidden = set(forbidden_codes)
    start = "0000"

    # Если стартовая комбинация запрещена или совпадает с целью
    if start in forbidden or start == target:
        return 0 if start == target else -1

    # BFS: (текущий_код, количество_шагов)
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current, steps = queue.popleft()

        # Генерируем все возможные следующие состояния (по одному разряду вперёд/назад)
        for i in range(4):
            for delta in (-1, 1):
                # Вычисляем новую цифру с учётом цикличности
                new_digit = str((int(current[i]) + delta + 10) % 10)
                new_code = current[:i] + new_digit + current[i+1:]

                # Если достигли цели — возвращаем шаги
                if new_code == target:
                    return steps + 1

                # Если не посещали и не запрещён — добавляем в очередь
                if new_code not in visited and new_code not in forbidden:
                    visited.add(new_code)
                    queue.append((new_code, steps + 1))

    # Если не нашли путь
    return -1


# === Ввод данных ===
m = int(input())
forbidden_codes = [input().strip() for _ in range(m)]
target = input().strip()

# === Решение ===
print(open_lock(m, forbidden_codes, target))