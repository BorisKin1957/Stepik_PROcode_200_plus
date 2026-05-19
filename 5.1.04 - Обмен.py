
flag = 'NO'

have_A = set(map(int, input().split()))
need_A = set(map(int, input().split()))

have_B = set(map(int, input().split()))
need_B = set(map(int, input().split()))

A_B = sorted(have_B & need_A)
B_A = sorted(need_B & have_A)

if A_B and B_A:
    flag = 'YES'

print(f'A->B: {' '.join(str(i) for i in A_B)}' if A_B else 'A->B: -')
print(f'B->A: {' '.join(str(i) for i in B_A)}' if B_A else 'B->A: -')
print(f'Обмен возможен: {flag}')