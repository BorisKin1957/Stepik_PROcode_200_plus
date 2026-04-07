'''
Задание
Строка 1: лента --> метки через пробел.

Строка 2: требование --> метки через запятую (пробелы допустимы).
Повторы означают кратность, напр.: α, β, β, γ.

Найди подстроку (непрерывное окно) S[L..R] минимальной длины, покрывающую
требование по кратностям (для каждой метки t её количество в окне ≥ требуемого).

Если существует несколько окон одинаковой длины, выбирай по приоритетам:

окно, в котором вся последовательность требования (с повторами) встречается как
подпоследовательность (в заданном порядке);

если всё ещё несколько --> окно, где порядок первых появлений различных требуемых 
меток совпадает с порядком в требовании;

если ничья --> возьми самое левое (с минимальным L).

Вывод: найденное окно (метки через пробел). Если решения нет --> выведи Пусто.

Разрешено только списки/векторы/срезы, линейный поиск индекса, счётчики в массивах. 
Без dict/map/set/heap.

🧪 Пример 1 — ввод

α β γ α δ β γ β
β, γ, α

                  
🧪 Пример 1 — вывод

β γ α
'''


ribbon = input().split()
pattern = input().split(', ')

n = len(ribbon)
len_p = len(pattern)

for i in range(len(ribbon)):
    cut = ribbon[i:i + len_p]
    if cut == pattern:
        print(*cut)
        exit(0)

labels, sublist, result = [], [], []

for i in range(len_p):
    if pattern[i] not in labels:
        labels.append(pattern[i])
        idxes = [pattern[i], []]
        for j in range(n):
            if ribbon[j] == pattern[i]:
                idxes[1].append(j)
        sublist.append(idxes)


for sym in pattern:
    for char, idx in sublist:
        if not idx:
            print('Пусто')
            exit(0)
        if char == sym:
            result.append(idx.pop(0))
            break

print(*ribbon[min(result):max(result) + 1])