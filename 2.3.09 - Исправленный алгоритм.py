route = list(map(int, input().split()))

if not route:
    print()
    print("Removed: 0")
    exit(0)

n = len(route)
result = [route[0]]

# Удалим подряд идущие дубли (они всё равно не нужны)
# Сделаем "уплотнение"
compressed = [route[0]]
for i in range(1, n):
    if route[i] != route[i-1]:
        compressed.append(route[i])

if len(compressed) == 1:
    print(compressed[0])
    print(f"Removed: {n - 1}")
    exit(0)

# Теперь строим зигзаг: добавляем, если текущий элемент "поворачивает"
result = [compressed[0], compressed[1]]
for i in range(2, len(compressed)):
    prev_diff = result[-1] - result[-2]
    curr_diff = compressed[i] - result[-1]
    if (prev_diff > 0 and curr_diff < 0) or (prev_diff < 0 and curr_diff > 0):
        result.append(compressed[i])

print(*result)
removed = n - len(result)
print(f"Removed: {removed}")