'''
Считай два целых числа r и c. Затем считай r строк, в каждой c элементов через
пробел. Выведи элементы матрицы в порядке обхода по спирали по часовой стрелке,
начиная с левого верхнего угла. Ответ выведи в одну строку через пробел.
Если r <= 0 или c <= 0, выведи пустую строку.

🧪 Пример 1 ввод

3 4
A B C D
E F G H
I J K L


🧪 Пример 1 вывод

A B C D H L K J I E F G
'''

n, m = map(int, input().split())

# Проверка на некорректные размеры
if n <= 0 or m <= 0:
    print('')
else:
    matrix = [input().split() for _ in range(n)]

    result = []
    top, bottom = 0, n - 1
    left, right = 0, m - 1

    while top <= bottom and left <= right:
        # Верхняя строка слева направо
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Правый столбец сверху вниз
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Нижняя строка справа налево (если есть строки)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Левый столбец снизу вверх (если есть столбцы)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    print(" ".join(result))