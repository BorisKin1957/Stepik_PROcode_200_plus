'''
Задание
Ввод: одна строка токенов через пробел. Допустимы якоря #, стоп-метки STOP, макросы с + (например Луг+Брод).

Требуется (строго в таком порядке):

Раскрыть макросы: каждый токен с + заменить на последовательность подметок (делается на месте).

Удалить все токены STOP.

Для каждого сегмента между # выполнить свёртку подряд идущих одинаковых меток в вид метка(xN) для N>1 (если N=1, оставить как есть). Якоря # сохраняются и не смешиваются с соседними сегментами.

Вывод: нормализованный ряд токенов в одну строку через пробел.

🧪 Пример 1 — ввод

Луг+Брод Брод Брод # STOP Роща Роща Роща # Мост+Перевал Мост


🧪 Пример 1 — вывод

Луг Брод(x3) # Роща(x3) # Мост Перевал Мост


Нажмите, чтобы увидеть тестовые данные
✅ Тест №2
Ввод

A+B B B # STOP C C


Вывод

A B(x3) # C(x2)


✅ Тест №3
Ввод

# A A A # STOP # X+X+Y Y


Вывод

# A(x3) # # X(x2) Y(x2)


✅ Тест №4
Ввод

Мост+Мост+Мост


Вывод

Мост(x3)


✅ Тест №5
Ввод

A STOP # B C STOP # STOP


Вывод

A # B C #
'''


# def roll_token(lst):
#     if lst == ['']:
#         return '#'
#     s = ''
#     for char, num in lst:
#         if num == 1:
#             s += f' {char}'
#         else:
#             s += f' {char}(x{num})'
#     return s
#
#
# string = input()
# string = string.replace('STOP', '')
#
# macros = list(map(str.strip, string.split('#')))
#
# result = []
#
# for token in macros:
#     token = token.strip().replace('+', ' ').split()
#
#     if token:
#         tmp = [[token[0], 1]]
#     else:
#         tmp = ['']
#
#     for i in range(1, len(token)):
#         count = 1
#         if token[i] == token[i - 1]:
#             if tmp[-1][0] == token[i]:
#                 tmp[-1][1] += 1
#             else:
#                 tmp.append([token[i], count + 1])
#         else:
#             tmp.append([token[i], count])
#
#     #print(tmp)
#     result.append(roll_token(tmp))
#
# result = ' '.join(result).strip().replace('  ', ' # ')
#
# print(result)

'''
Задание
...
'''

# Основная логика
string = input()

# Разделяем строку по пробелам, но сохраняем структуру якорей
tokens = string.split()

# Шаг 1: Раскрыть макросы (токены с '+')
expanded_tokens = []
for token in tokens:
    if '+' in token:
        expanded_tokens.extend(token.split('+'))
    else:
        expanded_tokens.append(token)

# Шаг 2: Удаляем только отдельно стоящие 'STOP'
filtered_tokens = [t for t in expanded_tokens if t != 'STOP']

# Шаг 3: Разделить по якорям '#', сохраняя пустые сегменты
segments = []
current_segment = []

for token in filtered_tokens:
    if token == '#':
        segments.append(current_segment)
        current_segment = []
    else:
        current_segment.append(token)
segments.append(current_segment)  # последний сегмент

# Шаг 4: Свернуть каждый сегмент
def compress(segment):
    if not segment:
        return []
    result = []
    prev = segment[0]
    count = 1
    for i in range(1, len(segment)):
        if segment[i] == prev:
            count += 1
        else:
            result.append(f"{prev}(x{count})" if count > 1 else prev)
            prev = segment[i]
            count = 1
    result.append(f"{prev}(x{count})" if count > 1 else prev)
    return result

compressed_segments = [compress(seg) for seg in segments]

# Шаг 5: Собрать результат, вставляя '#' между сегментами
output_parts = []
for i, comp_seg in enumerate(compressed_segments):
    if i > 0:
        output_parts.append('#')
    output_parts.extend(comp_seg)

# Формируем финальный вывод
result = ' '.join(output_parts)
print(result)