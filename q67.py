def first_unique(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None
s = "swiss"
print(first_unique(s))