# Инициализация словарей:
# users — хранит, за какой вариант голосует каждый пользователь: user → option
# options — хранит количество голосов за каждый вариант: option → count
users = {}
options = {}

# Считываем количество команд Q
for _ in range(int(input())):
    s = input().split()  # Разбиваем строку на части: команда, аргументы

    # === КОМАНДА VOTE: пользователь голосует за вариант ===
    if s[0] == 'VOTE':
        user, opt = s[1], s[2]  # Извлекаем имя пользователя и вариант

        # Проверяем, голосовал ли пользователь ранее
        if user in users:
            # Если он уже голосовал за ДРУГОЙ вариант
            if users[user] != opt:
                old_opt = users[user]  # Запоминаем старый вариант
                options[old_opt] -= 1  # Уменьшаем счётчик старого варианта
                users[user] = opt  # Обновляем голос пользователя
                options[opt] = options.get(opt, 0) + 1  # Увеличиваем счётчик нового варианта

        else:
            # Пользователь голосует впервые
            users[user] = opt  # Запоминаем его выбор
            options[opt] = options.get(opt, 0) + 1  # Увеличиваем счётчик

        print('OK')  # Всегда выводим OK при успешном VOTE

    # === КОМАНДА REVOKE: отмена голоса пользователя ===
    elif s[0] == 'REVOKE':
        user = s[1]  # Извлекаем имя пользователя

        # Если пользователь не голосовал — ошибка
        if user not in users:
            print('ERROR not-voted')
        else:
            # Получаем вариант, за который он голосовал
            voted_option = users[user]
            # Уменьшаем счётчик этого варианта
            options[voted_option] -= 1
            # Удаляем пользователя из списка проголосовавших
            del users[user]
            print('OK')

    # === КОМАНДА COUNT: вывести число голосов за вариант ===
    elif s[0] == 'COUNT':
        opt = s[1]  # Извлекаем вариант
        # Если вариант ещё не встречался — 0 голосов
        # Используем get, чтобы безопасно получить значение
        print(options.get(opt, 0))

    # === КОМАНДА TOP K: вывести до K лучших вариантов ===
    elif s[0] == 'TOP':
        k = int(s[1])  # Сколько вариантов нужно вывести
        # Фильтруем только те варианты, у которых count > 0
        positive_options = [(opt, cnt) for opt, cnt in options.items() if cnt > 0]

        # Сортируем: по убыванию count, при равенстве — лексикографически по имени
        positive_options.sort(key=lambda x: (-x[1], x[0]))

        # Если нет ни одного варианта с положительным счётом
        if not positive_options:
            print('-')
        else:
            # Берём не более чем k первых элементов
            for opt, cnt in positive_options[:k]:
                print(f'{opt}:{cnt}')