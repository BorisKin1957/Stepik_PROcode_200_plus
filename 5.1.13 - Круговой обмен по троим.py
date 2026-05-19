
data = []

for i in range(6):
    try:
        st = input().split()
        data.append(set(st))
    except EOFError:
        data.append(set())


A_have = data[0]
A_need = data[1]
B_have = data[2]
B_need = data[3]
C_have = data[4]
C_need = data[5]

AB = A_need & B_have
BC = B_need & C_have
CA = C_need & A_have

if AB and BC and CA:
    flag = 'YES'
else:
    flag = 'NO'

print(f"A->B: {' '.join(sorted(AB))}" if AB else 'A->B: -')
print(f"B->C: {' '.join(sorted(BC))}" if BC else 'B->C: -')
print(f"C->A: {' '.join(sorted(CA))}" if CA else 'C->A: -')

print(f'Цикл возможен: {flag}')