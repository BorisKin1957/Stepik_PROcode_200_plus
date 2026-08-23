
try:
    s = input()
except EOFError:
    exit()

# Если строка меньше 3 символов, троек быть не может
if len(s) < 3:
    print(0)
    exit()

# Словари для хранения первого и последнего вхождения символов
first_occurrence = {}
last_occurrence = {}

for i, char in enumerate(s):
    if char not in first_occurrence:
        first_occurrence[char] = i
    last_occurrence[char] = i

# Множество для хранения уникальных пар (c1, c2)
unique_pairs = set()

# Перебираем все уникальные символы, встречающиеся в строке
for char in first_occurrence:
    first_idx = first_occurrence[char]
    last_idx = last_occurrence[char]

    # Если символ встречается хотя бы дважды (между первым и последним вхождением есть место)
    if first_idx < last_idx:
        c1 = char
        # Берем все символы, которые находятся строго между первым и последним вхождением c1
        # Они могут служить символом c2
        middle_symbols = set(s[first_idx + 1: last_idx])

        for c2 in middle_symbols:
            unique_pairs.add((c1, c2))

# Выводим количество уникальных троек
print(len(unique_pairs))

