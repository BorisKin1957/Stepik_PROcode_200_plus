
n = int(input())
words = [list(input()) for _ in range(n)]

anagrams = []

words.sort(key=lambda x: sorted(x))

tmp = [words[0]]

for i in range(1, n):
    if sorted(words[i]) == sorted(tmp[-1]):
         tmp.append(words[i])
         continue
    anagrams.append(sorted(tmp))
    anagrams.append([''])
    tmp = [words[i]]

anagrams.append(sorted(tmp))

for lst in anagrams:
    for word in lst:
        print(''.join(word))





