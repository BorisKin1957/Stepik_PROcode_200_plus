

s = input()
m = int(input())

words = [input().strip() for _ in range(m)]
L = len(words[0])

result = []

for i in range(len(s)):
    s_slice = s[i: i + m * L]
    word_set = []
    for j in range(0, m * L, L):
        word_set.append(s_slice[j: j + L])
    if set(words) == set(word_set):
        result.append(i)

print(*result if result else '-')



