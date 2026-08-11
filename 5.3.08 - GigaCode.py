'''
В первой строке даны два числа R и C -- размеры карты.
Далее идут R строк, каждая длиной C, состоящая из символов 0 и 1.

1 обозначает сушу,

0 обозначает воду.

Остров -- это связная область клеток 1, соединённых по сторонам (4-соседям).

Два острова считаются одинаковыми, если их формы совпадают с точностью до сдвига
(повороты и отражения не учитываются).

Нужно найти и вывести количество различных форм островов.

🧪 Примеры ввода/вывода
Пример 1

3 5
11000
11000
00110


2


Пример 2

1 1
0


0


Пример 3

3 3
111
101
111


1
'''


def count_distinct_islands():
    # Считываем размеры карты R и C
    R, C = map(int, input().split())

    # Считываем саму карту
    grid = []
    for _ in range(R):
        grid.append(input().strip())

    # Если карта пустая, возвращаем 0 островов
    if R == 0 or C == 0:
        print(0)
        return

    # Направления для обхода (вверх, вправо, вниз, влево)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Множество для хранения уникальных форм островов
    unique_islands = set()

    # Функция для приведения формы острова к каноническому виду (нормализации)
    def normalize_island(cells):
        # Если остров пустой, возвращаем пустой кортеж
        if not cells:
            return tuple()

        # Находим минимальные координаты (самая левая верхняя клетка)
        min_row = min(cell[0] for cell in cells)
        min_col = min(cell[1] for cell in cells)

        # Нормализуем координаты, сдвигая остров так, чтобы минимальная клетка была в (0, 0)
        normalized = []
        for row, col in cells:
            normalized.append((row - min_row, col - min_col))

        # Сортируем для получения упорядоченного представления
        normalized.sort()

        # Преобразуем в кортеж для возможности хранения в множестве
        return tuple(normalized)

    # DFS для поиска связных компонентов (островов)
    def dfs(r, c, visited):
        stack = [(r, c)]
        visited.add((r, c))
        island_cells = [(r, c)]  # Сохраняем все клетки острова

        while stack:
            curr_r, curr_c = stack.pop()

            # Проверяем всех 4-соседей
            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc

                # Если сосед внутри границ и является частью острова
                if (0 <= nr < R and 0 <= nc < C and
                        grid[nr][nc] == '1' and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    stack.append((nr, nc))
                    island_cells.append((nr, nc))

        return island_cells

    # Множество для отслеживания посещенных клеток
    visited = set()

    # Проходим по всем клеткам
    for r in range(R):
        for c in range(C):
            # Если нашли часть острова и не посещали её
            if grid[r][c] == '1' and (r, c) not in visited:
                # Найти все клетки острова
                island_cells = dfs(r, c, visited)

                # Привести форму острова к каноническому виду
                normalized_form = normalize_island(island_cells)

                # Добавить в множество уникальных форм
                unique_islands.add(normalized_form)

    # Вывести количество уникальных форм островов
    print(len(unique_islands))


# Запускаем функцию
count_distinct_islands()