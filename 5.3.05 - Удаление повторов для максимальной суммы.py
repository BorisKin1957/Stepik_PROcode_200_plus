'''
Считай список чисел через пробел.

Найди подмассив (последовательные элементы), в котором нет повторяющихся чисел,
и сумма элементов максимальна.

Выведи эту максимальную сумму.
'''

numbers = list(map(int, input().split()))

max_sum = 0
left = 0
current_sum = 0
seen = set()

for right, num in enumerate(numbers):
    # Если число повторяется, сдвигаем левый край
    while num in seen:
        seen.remove(numbers[left])
        current_sum -= numbers[left]
        left += 1

    # Добавляем новое число
    seen.add(num)
    current_sum += num
    max_sum = max(max_sum, current_sum)

print(max_sum)