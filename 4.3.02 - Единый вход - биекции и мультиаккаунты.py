'''
История
Выкатили соцвходы: email, телефон и OAuth. У одного пользователя может быть
несколько идентификаторов и один аккаунт; а один идентификатор -- максимум за
одним аккаунтом. Поддержке важно быстро находить владельца по любому id и не
допускать «перехвата» уже привязанного идентификатора.

🎯 Задание
Что на входе
Сначала целое Q. Далее ровно Q строк-команд вида:

LINK acc id

UNLINK acc id

FIND id

acc и id -- строки без пробелов. Примеры id: mail:a@x, phone:+1, oauth:vk:42.

Что храним внутри
Две структуры:

acc -> set(ids) -- у каждого аккаунта набор привязанных идентификаторов;

id -> acc -- обратная мапа, по идентификатору узнаём, к какому аккаунту он привязан.

Поведение команд

Шаг 1. LINK acc id
Привязать id к аккаунту acc.

Если id не привязан ни к кому → привязываем к acc, печатаем OK.

Если id уже привязан к этому же acc → ничего не меняем, печатаем OK.

Если id привязан к другому аккаунту owner → печатаем
ERROR already-linked owner.

Шаг 2. UNLINK acc id
Отвязать id от аккаунта acc.

Если id действительно привязан к acc → отвязываем, печатаем OK.

Иначе (нет такого id, или id привязан к другому аккаунту) → печатаем
ERROR not-linked.

Примечание: если после отвязки у acc не осталось идентификаторов, это не влияет
на дальнейшую работу. Пустой аккаунт можно не хранить.

Шаг 3. FIND id
Найти аккаунт по id и показать все его идентификаторы.

Если id не найден в id -> acc → печатаем -.

Иначе печатаем строку:
acc: id1,id2,...
где перечислены все идентификаторы, привязанные к этому acc, в лексикографическом
порядке по обычному сравнению строк; без пробелов после запятых.

Формат вывода (строго):

OK -- для успешных LINK/UNLINK.

ERROR already-linked <owner> -- для конфликтного LINK.

ERROR not-linked -- для некорректного UNLINK.

acc: id1,id2,... или - -- для FIND.

Дополнительные уточнения

Команды и аргументы чувствительны к регистру.

Обрабатываем ровно Q команд, по одной строке вывода на команду.

Порядок вывода идентификаторов при FIND -- строго по возрастанию лексикографически
(например: id10 > id2, потому что сравнение посимвольное).

Пример 2 — ввод

10
LINK u1 mail:a@x
LINK u1 phone:+2
LINK u2 phone:+2
FIND phone:+2
UNLINK u2 phone:+2
UNLINK u1 phone:+2
FIND phone:+2
LINK u2 phone:+2
FIND mail:a@x
FIND phone:+2


🧪 Пример 2 — вывод

OK
OK
ERROR already-linked u1
u1: mail:a@x,phone:+2
ERROR not-linked
OK
-
OK
u1: mail:a@x
u2: phone:+2
'''

q = int(input())

# acc_base: отображает аккаунт -> множество идентификаторов (set)
acc_base = {}

# iden_base: отображает идентификатор -> аккаунт (обратная связь)
iden_base = {}

for _ in range(q):
    # Разбиваем строку на части и убираем лишние пробелы
    parts = [s.strip() for s in input().split()]

    # Команда FIND имеет 2 аргумента: "FIND id"
    if len(parts) == 2:
        cmd, iden = parts[0], parts[1]

        # Если идентификатор не найден в обратной мапе
        if iden not in iden_base:
            print('-')
        else:
            # Находим владельца
            owner = iden_base[iden]
            # Получаем все идентификаторы этого аккаунта
            identifiers = acc_base[owner]
            # Сортируем лексикографически
            sorted_ids = sorted(identifiers)
            print(f'{owner}: {",".join(sorted_ids)}')

    # Команды LINK и UNLINK имеют 3 аргумента: "LINK/UNLINK acc id"
    else:
        cmd, acc, iden = parts[0], parts[1], parts[2]

        if cmd == 'LINK':
            # Если идентификатор ещё не привязан ни к кому
            if iden not in iden_base:
                # Добавляем привязку: id -> acc
                iden_base[iden] = acc
                # Добавляем id в множество идентификаторов аккаунта acc
                if acc not in acc_base:
                    acc_base[acc] = set()
                acc_base[acc].add(iden)
                print('OK')

            # Если идентификатор уже привязан к этому же аккаунту
            elif iden_base[iden] == acc:
                print('OK')

            # Если идентификатор привязан к другому аккаунту
            else:
                owner = iden_base[iden]
                print(f'ERROR already-linked {owner}')

        elif cmd == 'UNLINK':
            # Проверяем, что идентификатор привязан именно к этому аккаунту
            if iden in iden_base and iden_base[iden] == acc:
                # Удаляем запись из обратной мапы
                del iden_base[iden]
                # Удаляем идентификатор из множества аккаунта
                acc_base[acc].discard(iden)

                # Если у аккаунта не осталось идентификаторов, можно удалить его
                if len(acc_base[acc]) == 0:
                    del acc_base[acc]  # по условию можно не хранить пустые аккаунты

                print('OK')
            else:
                # Либо id не существует, либо привязан к другому аккаунту
                print('ERROR not-linked')

# print()
# print(f'База данных аккаунтов: {acc_base}')
# print(f'База идентификаторов: {iden_base}')
