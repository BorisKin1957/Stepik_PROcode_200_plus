
try:
    word = input()
except EOFError:
    print(0)
    exit()

if not word:
    print(0)
    exit()

n = len(word)

slices = []
tmp = [word[0]]

for i in range(1, n):
    if word[i] not in tmp:
        tmp.append(word[i])
    else:
        slices.append(tmp)
        tmp = [word[i]]
        
slices.append(tmp)

result = ''.join(max(slices, key=len))

print(len(result), result, sep='\n')