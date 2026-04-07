'''
Задание
Строка 1: исходные метки через пробел (могут быть любыми строками;
допускается пустая строка).

Строка 2: целое N --> число итераций (N ≥ 0).

На каждой итерации заменяй каждую максимальную серию одинаковых меток t длины
k на два токена: str(k) и t.

Вывод: результат после N итераций в одну строку через пробел (если итог пуст -->
вывести пустую строку).

Ограничения по инструментам: только списки/векторы/срезы и примитивные операции
над ними; без dict/map/set/heap и без рекурсии.

Нажмите, чтобы увидеть тестовые данные
Sample Input:

Луг Луг Роща
2
Sample Output:

1 2 1 Луг 1 1 1 Роща
'''


scroll = list(map(str.strip, input().split()))
n = int(input())

for _ in range(n):
    if not scroll:
        break
    result = []
    tmp = [0, scroll[0]]
    for i in range(len(scroll)):
        if scroll[i] == tmp[1]:
            tmp[0] += 1
        else:
            result.extend(tmp)
            tmp = [1, scroll[i]]
    result.extend(tmp)
    scroll = result[:]
    result = []

print(*scroll)
