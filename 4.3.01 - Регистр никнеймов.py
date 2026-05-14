# Функция канонизации имени: преобразует никнейм в "каноническую" форму
def cyrillic_to_latin(nic_raw, map, mapping):
    canon_nic = ''  # Будущий канонизированный ник

    # Проходим по каждому символу исходного ника
    for char in nic_raw:
        if char in map:  # Если символ есть в пользовательской карте замен (приоритет выше)
            canon_nic += map[char]
        elif char in mapping:  # Иначе — проверяем фолбэк (стандартные замены кириллица→латиница)
            canon_nic += mapping[char]
        else:  # Если нет ни в одной из карт — оставляем символ как есть
            canon_nic += char

    return canon_nic  # Возвращаем канонизированное имя

# Стандартная карта замен для "двойников" кириллица → латиница
mapping = {
    'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'М': 'M', 'Н': 'H',
    'О': 'O', 'Р': 'R', 'С': 'S', 'Т': 'T', 'Х': 'X', 'У': 'Y',
    'а': 'a', 'в': 'b', 'е': 'e', 'к': 'k', 'м': 'm', 'н': 'h',
    'о': 'o', 'р': 'r', 'с': 's', 'т': 't', 'х': 'x', 'у': 'y'
}

# Читаем строку с пользовательскими заменами
tmp = input().split(', ')  # Разбиваем по запятой на пары
map = {}  # Карта пользовательских замен

# Обрабатываем каждую пару src->dst
for i in range(len(tmp)):
    k, v = tmp[i].split('->')  # Разделяем по стрелке
    map[k] = v.strip()  # Ключ — исходный символ, значение — замена (убираем пробелы)

q = int(input())  # Число операций

# waiting_line — очередь ожидания для каждого канона: {канон: [userId1, userId2, ...]}
waiting_line = {}

# canon_base — база: какой канон принадлежит какому пользователю: {канон: userId}
canon_base = {}

# user_base — база: у какого пользователя какой активный канон: {userId: канон}
user_base = {}

# Обработка q операций
for _ in range(q):
    line = [s.strip() for s in input().split()]  # Разбиваем строку команды на токены

    # Команда WHO: один аргумент после команды — имя
    if len(line) == 2:
        # Канонизируем имя
        canon = cyrillic_to_latin(line[-1].strip(), map, mapping)
        # Ищем владельца канона; если нет — выводим NOTFOUND
        print(canon_base.get(canon, 'NOTFOUND'))

    else:
        func = line[0]  # Тип команды: ADD или RENAME

        if func == 'ADD':
            nic_raw, user = line[1], line[2]  # Исходное имя и ID пользователя
            canon = cyrillic_to_latin(nic_raw, map, mapping)  # Канонизация

            # Если канон свободен И у пользователя нет активного канона
            if not canon_base.get(canon) and not user_base.get(user):
                canon_base[canon] = user  # Занимаем канон
                user_base[user] = canon     # Назначаем пользователю
                print('OK')

            else:
                # Если у пользователя уже есть активный канон (это переезд)
                if user_base.get(user):
                    # Получаем старое имя пользователя
                    free_name = user_base.get(user)
                    # Меняем его канон на новый
                    user_base[user] = canon
                    # Освобождаем старый канон
                    canon_base.pop(free_name)
                    # Занимаем новый
                    canon_base[canon] = user

                    # Если кто-то ждал освобождения старого канона
                    if free_name in waiting_line:
                        who = waiting_line.pop(free_name)[0]  # Берём первого из очереди
                        user_base[who] = free_name           # Даём ему канон
                        canon_base[free_name] = who       # Обновляем базу

                    print('OK')

                else:
                    # У пользователя нет канона, но канон занят другим
                    if canon_base.get(canon) != user:
                        who = canon_base[canon]  # Владелец канона
                        print(f'CONFLICT {who}')
                        # Добавляем пользователя в очередь на этот канон (без дублей)
                        waiting_line[canon] = waiting_line.get(canon, []) + [user]

                    else:
                        if waiting_line.get(canon):
                            user = waiting_line.pop(canon)[0]
                            canon_base[canon] = user

        elif func == 'RENAME':
            user, nic_raw = line[1], line[2]  # userId и новое имя
            canon = cyrillic_to_latin(nic_raw, map, mapping)  # Канон нового имени

            # Если пользователя нет — NOTFOUND
            if not user_base.get(user):
                print('NOTFOUND')

            else:
                # Если новый канон уже занят — CONFLICT
                if canon_base.get(canon):
                    print(f'CONFLICT {canon_base[canon]}')
                else:
                    free_name = user_base.pop(user)  # Удаляем старый канон у пользователя

                    # Если кто-то ждал освобождения старого канона
                    if waiting_line.get(free_name):
                        who = waiting_line.pop(free_name)[0]  # Первый в очереди
                        canon_base[free_name] = who       # Даём ему канон
                        user_base[who] = free_name           # Назначаем ему

                        # Присваиваем пользователю новый канон
                        canon_base[canon] = user
                        user_base[user] = canon
                    else:
                        # Освобождаем старый канон
                        canon_base.pop(free_name)
                        # Назначаем новый
                        canon_base[canon] = user
                        user_base[user] = canon

                    print('OK')

# Эти строки закомментированы — для отладки
# print()
# print(f'Лист ожидания: {waiting_line}')
# print(f'База никнеймов: {canon_base}')
# print(f'База пользователей: {user_base}')
