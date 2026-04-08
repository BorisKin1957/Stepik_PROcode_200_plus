'''
Ввод: одна строка целых чисел через пробел (ввод может быть пустым).
Нужно: вывести одну строго возрастающую подпоследовательность максимальной длины.

Правило выбора единственного ответа:
среди всех подпоследовательностей максимальной длины выберите ту, которая лексикографически
минимальна по значениям (то есть минимальный последний элемент; при равенстве -- минимальный
предпоследний и т. д.). Это делает ответ уникальным, например для 10 9 2 5 3 7 101 18
требуется 2 3 7 18.

Вывод:

    если числа есть → на первой строке подпоследовательность через пробел, на следующей
    строке → Length: L;

    если ввода нет → вывести только Length: 0 (без пустой строки выше).



    Подсказка терминов: подпоследовательность → элементы исходного массива в порядке
    возрастания индексов и значений (i1 < i2 < ... и a[i1] < a[i2] < ...).

    Ограничения:
    разрешены только списки/векторы/срезы, ручной двоичный поиск и финальный reverse.
    Без словарей, множеств и т. п.
    Запрещены лишние пробелы в конце строк.

'''

# Костыль в угоду способа проверки теста 4
try:
    numbers = list(map(int, input().split()))
except EOFError:
    print('Length: 0')
    exit(0)

n = len(numbers)
results, i = [], 0

if numbers and min(numbers) == max(numbers):
    results = [[0, [numbers[0]]]]

else:
    while numbers:
        min_num = min(numbers)
        lst = [min_num]
        sub = [i, lst]
        ind = numbers.index(min_num)
        cut = numbers[ind + 1:]
        numbers.remove(min_num)
        while cut:
            min_num += 1
            for num in cut:
                if num == min_num:
                    lst.append(num)
                    numbers.remove(num)
                    cut = cut[cut.index(num) + 1:]
                    min_num += 1
            n -= 1

        results.append(sub)
        i += 1

if results:
    result = results[0][1]
    print(*result)
else:
    result = []

count = len(result)

print(f'Length: {count}')



