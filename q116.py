def count(n):
    if n < 10:
        return 1
    return 1 + count(n // 10)
n = 1234
print(count(n))