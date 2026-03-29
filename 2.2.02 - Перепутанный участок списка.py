

people = input().split(', ')

n = len(people)
start, end = int(input()), int(input())

start = min(max(start, 0), n)
end = min(max(end, 0), n)
if start < end:
    result = people[:start] + sorted(people[start:end]) + people[end:]
else:
    result = people

print(*result, sep='\n')