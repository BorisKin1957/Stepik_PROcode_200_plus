

'''
Дано число n (1 ≤ n ≤ 12).

Нужно посчитать, сколько существует способов расставить n ферзей на шахматной
доске размера n × n так, чтобы ни один ферзь не бил другого.

Напомним: ферзь бьёт все клетки по вертикали, горизонтали и диагоналям.

Выведи количество таких расстановок.
'''


# ... existing code ...

def solve_n_queens(n):
    """
    Возвращает количество способов расставить n ферзей на доске n×n,
    чтобы ни один не бил другого.
    """

    def backtrack(row, cols, diag1, diag2):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            # col — столбец, col - row — главная диагональ, col + row — побочная
            if col not in cols and (col - row) not in diag1 and (col + row) not in diag2:
                # Пробуем поставить ферзя в (row, col)
                cols.add(col)
                diag1.add(col - row)
                diag2.add(col + row)
                count += backtrack(row + 1, cols, diag1, diag2)
                # Откат
                cols.remove(col)
                diag1.remove(col - row)
                diag2.remove(col + row)
        return count

    return backtrack(0, set(), set(), set())


n = int(input().strip())
print(solve_n_queens(n))
