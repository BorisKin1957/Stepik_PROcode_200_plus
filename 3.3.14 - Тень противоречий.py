'''
Строка 1: целое M. Далее M строк A B (имена без пробелов): дуга означает, что A сильнее B.
Все встретившиеся имена считаются вершинами графа. Выведите либо НЕТ (если есть цикл),
либо две строки: ДА и на следующей любой корректный топологический порядок всех участников
через пробел. Если вершин нет (M=0), выведите ДА.
Пример 1

4
A B
B C
C D
D E


ДА
A B C D E
'''

M = int(input())

# Граф и степени входа
graph = {}
in_degree = {}
tops = set()

# Чтение рёбер
for _ in range(M):
    up, down = input().split()
    tops.add(up)
    tops.add(down)

    if up not in graph:
        graph[up] = []
    graph[up].append(down)

    # Инициализируем степени входа
    if up not in in_degree:
        in_degree[up] = 0
    if down not in in_degree:
        in_degree[down] = 0
    in_degree[down] += 1

# Находим все вершины с нулевой степенью входа
queue = []
for node in tops:
    if in_degree.get(node, 0) == 0:
        queue.append(node)

top_order = []

i = 0
while i < len(queue):
    current = queue[i]
    top_order.append(current)
    i += 1

    # Обновляем степени соседей
    if current in graph:
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

# Проверяем цикл
if len(top_order) != len(tops):
    print('НЕТ')
else:
    print('ДА')
    if top_order:
        print(*top_order)
    else:
        print()  # если нет ни одной вершины