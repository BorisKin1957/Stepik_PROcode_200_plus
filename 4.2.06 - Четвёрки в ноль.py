

array = [[int(num) for num in input().split()] for _ in range(4)]

result = 0

for num_0 in array[0]:
    for num_1 in array[1]:
        for num_2 in array[2]:
            for num_3 in array[3]:
                if num_0 + num_1 + num_2 + num_3 == 0:
                    result += 1

print(result)