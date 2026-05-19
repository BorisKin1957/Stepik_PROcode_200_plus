try:
    you = set(input().split())
except EOFError:
    you = set()

try:
    guy = set(input().split())
except EOFError:
    guy = set()

guy -= you

if guy:
    print('Покрою полностью: NO')
    print(f"Останется: {' '.join(sorted(guy))}")
else:
    print('Покрою полностью: YES')
    print('Останется: -')