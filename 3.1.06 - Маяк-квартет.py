

token, k = input(), int(input())

if k:
    result = tuple((f'{token} '* k).strip().split())

    print(*result)