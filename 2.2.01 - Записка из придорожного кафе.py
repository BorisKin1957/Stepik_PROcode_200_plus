

names = [name.strip() for name in input().split(',') if name.strip()]

print(*names, sep='\n') if names else print('Пусто')