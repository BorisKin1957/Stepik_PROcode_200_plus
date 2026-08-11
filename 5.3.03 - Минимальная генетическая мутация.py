'''
Задание
Работаем с цепочками ДНК длиной 8 символов (буквы A, C, G, T).

В первой строке задана начальная цепочка start.

Во второй строке -- целевая цепочка end.

В третьей строке -- число n.

Далее следуют n строк -- список допустимых цепочек (банк).

За один шаг можно изменить ровно один символ в текущей цепочке.
Новая цепочка после каждого шага обязана входить в банк.

Нужно найти минимальное количество шагов для превращения start в end.
Если это невозможно, выведи -1.

🧪 Примеры ввода/вывода
Тестовые данные
№ Теста
Входные данные
Выходные данные
1

AACCGGTT
AACCGGTA
1
AACCGGTA

1
'''

from collections import deque

def min_mutation(start, end, bank):
    bank_set = set(bank)
    if end not in bank_set:
        return -1

    # Если start совпадает с end — уже на месте
    if start == end:
        return 0

    # BFS: (текущая_цепочка, количество_шагов)
    queue = deque([(start, 0)])
    visited = {start}
    genes = ['A', 'C', 'G', 'T']  # возможные символы

    while queue:
        current, steps = queue.popleft()

        # Пробуем изменить каждый символ
        for i in range(len(current)):
            for gene in genes:
                # Строго одно изменение: отличаемся в позиции i
                if gene == current[i]:
                    continue
                new_mutation = current[:i] + gene + current[i+1:]

                # Если достигли цели
                if new_mutation == end:
                    return steps + 1

                # Если новая цепочка в банке и не посещена
                if new_mutation in bank_set and new_mutation not in visited:
                    visited.add(new_mutation)
                    queue.append((new_mutation, steps + 1))

    return -1


# === Ввод данных ===
start = input().strip()
end = input().strip()
n = int(input())
bank = [input().strip() for _ in range(n)]

# === Решение ===
print(min_mutation(start, end, bank))