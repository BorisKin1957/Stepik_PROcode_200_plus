

names = list(map(str.strip, input().split(',')))
target = input().strip()

result = [name for name in names if name != target]

print('\n'.join(result) if result else 'Пусто')

