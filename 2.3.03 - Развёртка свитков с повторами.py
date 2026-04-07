


def decode_string(s):
    stack = []
    current_str = ''   # текущая раскодированная строка
    current_num = 0    # текущее число повторений

    for char in s:
        if char.isdigit():
            # При чтении каждой новой цифры — "сдвигаем" текущее число влево
            # (умножаем на 10) и добавляем новую цифру.
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Сохраняем текущее состояние
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            # Повторяем текущую строку num раз, разделяя пробелами
            repeated = " ".join([current_str] * num) if num > 0 else ''
            # Объединяем с предыдущей строкой
            if prev_str and repeated:
                current_str = prev_str + " " + repeated
            else:
                current_str = prev_str + repeated
        else:
            current_str += char
    # Возвращаем строку, удаляя лишние пробелы от сцепления строк
    return ' '.join(current_str.split())

result = decode_string(input())

print(result)