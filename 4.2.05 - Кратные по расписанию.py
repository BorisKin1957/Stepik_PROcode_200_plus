

array = list(map(int, input().split()))
k = int(input())

n = len(array)
flag = False

for i in range(n):
    summ = []
    for j in range(i, n):
        summ.append(array[j])
        # Проверяем длину подмассива и условие делимости
        if len(summ) > 1:
            if (k == 0 and sum(summ) == 0) or (k != 0 and sum(summ) % k == 0):
                flag = True
                break
    if flag:
        break  # Выход из внешнего цикла при нахождении подходящего подмассива

print('YES' if flag else 'NO')