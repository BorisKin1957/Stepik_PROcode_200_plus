

n = int(input())

words = {}

for word in input().split():
    words[word] = words.get(word, 0) + 1

k = int(input())

if k <= 0 or n == 0:
    exit()

result = sorted(words.items(), key=lambda x: (-x[1], x[0]))

if len(result) > k:
    result = result[:k]

for word, count in result:
    print(word)
