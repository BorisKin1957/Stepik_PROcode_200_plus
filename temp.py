string = '# A A A # STOP # X+X+Y Y'
string = string.replace('STOP ', '#')
macros = list(map(str.strip, string.split('#')))

for token in macros:

    token = token.strip().replace('+', ' ').split()
    #token = token.replace('STOP', '').split()



    if token:
        tmp = [[token[0], 1]]
    else:
        tmp = []

    for i in range(1, len(token)):
        count = 1
        if token[i] == token[i - 1]:
            if tmp[-1][0] == token[i]:
                tmp[-1][1] += 1
            else:
                tmp.append([token[i], count + 1])

        else:
            # if tmp:
            #     tmp.append([token[i], count])
            # else:
            #     tmp.append([token[i - 1], count])
            tmp.append([token[i], count])



    print(tmp)

# lst = [[['A', 1]], [['B', 1], ['C', 1]], []]
#
# res = sum(lst, [])
#
# print(res)