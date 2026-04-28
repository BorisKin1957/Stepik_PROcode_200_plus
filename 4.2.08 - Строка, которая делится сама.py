try:
    string = input()
    n = len(string)
    all_idx = {char: string.rindex(char) for char in string}
    idx = all_idx[string[0]]
except (EOFError, IndexError):
    print()
    exit()

segments = []

part = string[:idx + 1]

for i in range(1, n):
    char = string[i]
    last = all_idx[char]
    if char in part:
        if last > all_idx[part[-1]]:
            add = string[all_idx[part[-1]] + 1:last + 1]
            part += add
    else:
        segments.append(part)
        idx = all_idx[char]
        part = string[i:idx + 1]

segments.append(part)

result = [len(part) for part in segments]

print(*result)

