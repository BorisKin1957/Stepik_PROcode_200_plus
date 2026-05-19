

st_1 = set(map(int, input().split()))
st_2 = set(map(int, input().split()))

st_1 &= st_2

print(*sorted(st_1)) if st_1 else print('Нет общих')
