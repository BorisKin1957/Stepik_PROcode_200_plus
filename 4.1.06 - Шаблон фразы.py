

from collections import Counter

pattern = Counter(input())
pattern_vol = sorted(pattern.values())

text = Counter(input().split())
text_vol = sorted(text.values())

print('YES' if pattern_vol == text_vol else 'NO')