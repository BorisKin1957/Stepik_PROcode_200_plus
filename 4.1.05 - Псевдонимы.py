

from collections import Counter

s = Counter(input())
s_ = sorted(s.values())

t = Counter(input())
t_ = sorted(t.values())

print('YES' if s_ == t_ else 'NO')