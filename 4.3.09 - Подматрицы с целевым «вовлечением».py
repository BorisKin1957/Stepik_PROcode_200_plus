
# возвращает все подматрицы матрицы
def get_submatrices(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Перебираем все возможные пары (top, bottom) — диапазон строк
    for top in range(rows):
        for bottom in range(top, rows):
            # Перебираем все возможные пары (left, right) — диапазон столбцов
            for left in range(cols):
                for right in range(left, cols):
                    # Теперь извлекаем подматрицу от (top, left) до (bottom, right)
                    submatrix = []
                    for i in range(top, bottom + 1):
                        row = []
                        for j in range(left, right + 1):
                            row.append(matrix[i][j])
                        submatrix.append(row)

                    yield submatrix

# возвращает сумму чисел из списка
def get_list_sum(lst):
    list_sum = 0
    for item in lst:
        list_sum += sum(item)

    return list_sum
    

r = int(input().split()[0])

matrix = [[int(i) for i in input().split()] for _ in range(r)]

T = int(input())

result = 0

for sub in get_submatrices(matrix):
    if get_list_sum(sub) == T:
        result += 1

print(result)