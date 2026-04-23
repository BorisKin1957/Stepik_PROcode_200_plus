def is_crossing(s1, e1, s2, e2):
    if s2 < s1 < e2 or s2 < e1 < e2 or s1 < s2 < e1 or s1 < e2 < e1:
        return True