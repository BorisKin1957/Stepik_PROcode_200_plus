'''Считай целые числа через пробел.
Выведи все уникальные тройки x y z (по одной тройке в строке), где x + y + z = 0
и внутри тройки выполнено x ≤ y ≤ z. Порядок строк лексикографический.
Если подходящих троек нет, то выведи Пусто.'''


numbers = sorted(map(int, input().split()))
n = len(numbers)
result = []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            vol = numbers[i], numbers[j], numbers[k]
            if sum(vol) == 0 and vol not in result:
                result.append(vol)


if result:
    for vol in result:
        print(*vol)
else:
    print('Пусто')

