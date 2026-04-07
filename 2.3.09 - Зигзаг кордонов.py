'''
Задание
Ввод: одна строка целых чисел через пробел (может быть пустой).

Построй зигзаг максимальной длины (удаляя минимум элементов).
Зигзаг: соседние разности чередуют знак; равные подряд значения не допускаются.

Вывод:

зигзаг одной строкой через пробел (если пусто --> пустая строка),

следующей строкой Removed: K, где K --> сколько элементов удалили.

Только операции списков/векторов/срезов; без словарей/множеств/куч и без рекурсии.

Пример 1 — ввод

1 7 4 9 2 5


🧪 Пример 1 — вывод

1 7 4 9 2 5
Removed: 0


Нажмите, чтобы увидеть тестовые данные
✅ Тест №2
Ввод

1 2 3 4 5


Вывод

1 5
Removed: 3


✅ Тест №3
Ввод

5 5 5 5


Вывод

5
Removed: 3


✅ Тест №4
Ввод

3 3 2 2 3 3 2


Вывод

3 2 3 2
Removed: 3


✅ Тест №5
Ввод

0 -1 1 -1 1 -1 1


Вывод

0 -1 1 -1 1 -1 1
Removed: 0
'''

route = list(map(int, input().split()))

# Определяем направление зигзага
for i in range(len(route) - 1):
    if route[i] > route[i + 1]:
        flag = ('-')
        break
    elif route[i] < route[i + 1]:
        flag = ('+')
        break
    # Если не удалось, то выводим результат и завершаем работу
    else:
        if i == len(route) - 2:
            print(route[0])
            print(f'Removed: {len(route) - 1}')
            exit(0)

result, removed = [route[0]], 0

# Проходим по точкам пути
for dote in route:
    if dote < result[-1]:
        if flag == '-':
            flag = '+'
            result.append(dote)
        else:
            removed += 1
            result.pop()
            result.append(dote)
    elif dote > result[-1]:
        if flag == '+':
            flag = '-'
            result.append(dote)
        else:
            removed += 1
            result.pop()
            result.append(dote)
    else:
        removed += 1

print(*result)
print(f'Removed: {removed - 1}')


