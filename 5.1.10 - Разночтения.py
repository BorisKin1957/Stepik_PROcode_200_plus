
try:
    scaner = set(input().split())
except EOFError:
    scaner = set()

try:
    magazin = set(input().split())
except EOFError:
    magazin = set()


only_scaner = sorted(scaner - magazin)
only_magazin = sorted(magazin - scaner)

print(f'Только у сканера: {' '.join(only_scaner)}' if only_scaner else 'Только у сканера: -')
print(f'Только в журнале: {' '.join(only_magazin)}' if only_magazin else 'Только в журнале: -')