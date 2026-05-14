import re

result = []
set_url = set()

for _ in range(int(input())):
    s = input().split()
    ts, url = int(s[0]), s[1]
    match = (re.search(r'.+(?=\?)', url))
    if match:
        cleaned_url = match.group(0)
    else:
        cleaned_url = url
    result_url = re.sub(r'/+$', '', cleaned_url)
    if result_url not in set_url:
        set_url.add(result_url)
        result.append([ts, result_url])

for url in sorted(result):
    print(*url)



