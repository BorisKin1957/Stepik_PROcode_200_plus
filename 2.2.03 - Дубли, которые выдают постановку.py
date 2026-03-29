

names = [name.strip() for name in input().split(', ')]
result = []

for name in names:
    if name not in result:
        result.append(name)

print(*result, sep='\n')
print(f'Удалено: {len(names) - len(result)}')
