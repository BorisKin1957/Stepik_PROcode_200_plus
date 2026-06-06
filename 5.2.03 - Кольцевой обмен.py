have_base = {}
need_base = {}

# Считываем данные
for _ in range(int(input())):
    name = input()
    s = input().split(': ')
    have = set(s[1].split())
    have_base[name] = have_base.get(name, have)
    s = input().split(': ')
    need = set(s[1].split())
    need_base[name] = need_base.get(name, need)

# Построим ориентированный граф: A -> B означает, что B имеет то, что нужно A
graph = {name: [] for name in have_base}

for A in need_base:
    for B in have_base:
        if A != B and need_base[A] & have_base[B]:
            graph[A].append(B)

# Функция поиска всех циклов длиной ≥3 через DFS
def find_cycles_dfs(start, current, path, visited, cycles):
    for neighbor in graph[current]:
        if neighbor == start and len(path) >= 3:
            # Нашли цикл длиной ≥3
            cycles.append(tuple(path[:]))  # сохраняем как кортеж
        elif neighbor not in visited and len(path) < len(graph):
            visited.add(neighbor)
            path.append(neighbor)
            find_cycles_dfs(start, neighbor, path, visited, cycles)
            path.pop()
            visited.remove(neighbor)

# Сбор всех циклов длиной ≥3
all_cycles = []
for name in graph:
    find_cycles_dfs(name, name, [name], {name}, all_cycles)

# Если циклов нет — выводим "Нет цикла."
if not all_cycles:
    print("Нет цикла")
    exit()

# Нормализация: для каждого цикла находим его лексикографически минимальное вращение
def normalize_cycle(cycle):
    n = len(cycle)
    # Все возможные вращения цикла
    rotations = [cycle[i:] + cycle[:i] for i in range(n)]
    # Возвращаем лексикографически наименьшее вращение как кортеж
    return min(rotations)

# Нормализуем все циклы и собираем уникальные
normalized_cycles = {normalize_cycle(cycle) for cycle in all_cycles}

# Выбираем лексикографически минимальный цикл из всех нормализованных
best_cycle = min(normalized_cycles)  # кортеж имён

# Форматируем вывод
chain = " -> ".join(best_cycle)
print(f"{chain} -> {best_cycle[0]}")