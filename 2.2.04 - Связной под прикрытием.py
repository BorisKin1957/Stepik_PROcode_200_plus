

names = list(map(str.strip, input().split(',')))
idx = int(input())

# Нормализуем idx:
# при idx < 0, результат выражения будет 0
# если idx > длины списка, результат равен длине списка
# Таким образом, избегаем ошибок выхода за пределы списка.
# иначе idx остается прежним
idx = max(0, min(idx, len(names)))

names.insert(idx, input().strip())

print(*names, sep='\n')