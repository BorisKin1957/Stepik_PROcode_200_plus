
code = input().split()

words = [input().lower() for _ in range(int(input()))]

code_page = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), code))

result = []

for word in words:
    new = ''
    for letter in word:
        new += code_page[letter]
    result.append(new)

print(len(set(result)))

