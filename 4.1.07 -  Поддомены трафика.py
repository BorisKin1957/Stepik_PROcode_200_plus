
domains = {}

for _ in range(int(input())):
    tmp = input().split()
    data = tmp[1].split('.')
    for i in range(len(data)):
        domains['.'.join(data[i:])] = domains.get('.'.join(data[i:]), 0) + int(tmp[0])

for domain, count in sorted(domains.items()):
    print(domain, count)

