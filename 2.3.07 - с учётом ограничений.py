'''
🎯 Задание (с учётом ограничений: только корзины, стабильные проходы, без словарей и компараторов)
Реализуем поразрядную сортировку (radix sort) справа налево — от младших позиций к старшим.
Неизвестные символы получают индекс = max_idx (идут в конец), известные — по порядку в alpha.
Слова с неизвестными символами выделяются отдельно и добавляются в конец результата (в порядке появления).
'''

# Считываем слова и чужой алфавит
string = list(map(str.strip, input().split()))
alpha = input().replace(' ', '')

# Максимальная длина слова — для выравнивания
m = len(max(string, key=len))
max_idx = len(alpha)  # Индекс для всех неизвестных букв

# Разделяем слова на "известные" и "содержащие неизвестные символы"
known_words = []
unknow_words = []

for word in string:
    if any(char not in alpha for char in word):
        unknow_words.append(word)  # Сохраняем порядок (стабильность)
    else:
        known_words.append(word)

# Выравниваем все известные слова до длины m, дополняя специальным значением (например, -1)
# Это нужно для поразрядной сортировки — чтобы сравнивать по всем позициям
padded_words = [list(word) + [''] * (m - len(word)) for word in known_words]


# Определяем функцию для получения "ключа" символа: его индекс в alpha или max_idx
def get_char_key(c):
    return alpha.index(c) if c in alpha else max_idx


# Поразрядная сортировка (radix sort) справа налево с использованием корзин
for pos in range(m - 1, -1, -1):  # от последнего символа к первому
    # Создаём корзины (0..max_idx), всего max_idx + 1 (учитываем неизвестные)
    buckets = [[] for _ in range(max_idx + 2)]  # +2: на всякий случай, включая max_idx

    for i, word in enumerate(padded_words):
        char = word[pos]
        if char == '':  # это дополненный символ — считаем как "минимум", т.е. префикс меньше
            key = -1  # хотим, чтобы пустые позиции (префиксы) шли в начало
        else:
            key = get_char_key(char)

        # Сдвигаем ключ, чтобы -1 стал 0, остальные — на 1 больше
        bucket_idx = key + 1
        buckets[bucket_idx].append(i)

    # Пересобираем порядок слов по корзинам (стабильно!)
    new_order = []
    for bucket in buckets:
        new_order.extend(bucket)

    # Обновляем порядок padded_words и known_words
    padded_words = [padded_words[i] for i in new_order]
    known_words = [known_words[i] for i in new_order]

# Формируем результат: сначала отсортированные известные слова, потом — неизвестные (в исходном порядке)
result = known_words + unknow_words

# Выводим через пробел
print(*result)