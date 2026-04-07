def custom_lexicographic_sort(words, alphabet):
    if not words:
        return []

    # Шаг 1: найти max длину
    max_len = max(len(word) for word in words)

    # Шаг 2: дополним слова до max_len символом '\0' (считаем его наименьшим)
    padded_words = []
    for word in words:
        padded = word + '\0' * (max_len - len(word))
        padded_words.append(padded)

    # Будем сортировать массив кортежей: (padded_word, original_word)
    arr = [(padded, orig) for padded, orig in zip(padded_words, words)]

    # Шаг 3: проходы справа налево (от последнего символа к первому)
    for pos in range(max_len - 1, -1, -1):
        # Создаём корзины — по одной на каждый символ алфавита + для '\0'
        # Индекс корзины = порядок символа в алфавите, '\0' будет в корзине 0
        buckets = [[] for _ in range(len(alphabet) + 1)]  # +1 для '\0'

        # Распределение по корзинам
        for padded, orig in arr:
            char = padded[pos]
            bucket_idx = 0  # для '\0'
            if char != '\0':
                # Найдём индекс символа в алфавите без map или dict
                for idx in range(len(alphabet)):
                    if alphabet[idx] == char:
                        bucket_idx = idx + 1  # +1 потому что 0 — для '\0'
                        break
            buckets[bucket_idx].append((padded, orig))

        # Сборка: вытягиваем из корзин по порядку
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

    # Извлекаем оригинальные слова
    result = [orig for padded, orig in arr]
    return result


words = ["caabbb", "aaa", "aabc"]
alphabet = "bca"

print(custom_lexicographic_sort(words, alphabet))