'''
В башне «Колокол» у каждого слова есть тайная лестница, ведущая к другому слову.
Но ступени у этой лестницы особенные: за раз можно изменить только одну букву,
и лишь так слово превращается в новое. Каждый шаг проверяется хранителями
словаря -- если промежуточного слова нет в списке дозволенных, лестница обрывается.

🎯 Задание
Сначала вводятся:

строка begin -- начальное слово,

строка end -- конечное слово,

число n,

затем n слов одинаковой длины (это словарь).

Можно за один шаг заменить в текущем слове ровно одну букву.
При этом новое слово должно существовать в словаре.

Нужно найти длину самой короткой цепочки преобразований от begin до end (включая оба этих слова).
Если добраться невозможно -- выведи 0.

🧪 Примеры ввода/вывода


Выходные данные
1

hit
cog
6
hot
dot
dog
got
log
cog

5
'''


def differs_by_one(word1, word2):
    """Проверяет, отличаются ли два слова ровно одной буквой"""
    if len(word1) != len(word2):
        return False
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    return diff_count == 1


def find_ladder(begin, end, dictionary):
    """
    Ищет цепочку слов от begin к end, где каждое слово отличается от предыдущего на одну букву.
    Возвращает длину цепочки или 0, если невозможно.
    """
    if begin == end:
        return 1

    word_set = set(dictionary)

    # Если end не в словаре, путь невозможен
    if end not in word_set:
        return 0

    # BFS от begin
    from collections import deque

    queue = deque([(begin, 1)])
    visited = {begin}

    while queue:
        current, length = queue.popleft()

        if current == end:
            return length

        # Перебираем все слова в словаре, которые можно получить из current
        for word in word_set:
            if word not in visited and differs_by_one(current, word):
                visited.add(word)
                queue.append((word, length + 1))

    return 0


# Ввод данных
begin = input().strip()
end = input().strip()
n = int(input())

dictionary = []
for _ in range(n):
    dictionary.append(input().strip())

# Решение
result = find_ladder(begin, end, dictionary)
print(result)
