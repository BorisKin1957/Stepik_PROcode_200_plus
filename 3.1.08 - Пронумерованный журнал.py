
# Для тех, кто брезгует условиями! ))
# Строим НЕИЗМЕНЯЕМУЮ последовательность пар
result = tuple(enumerate(input().split(), 1))

for i, name in result:
    print(f'{i}:{name}')