def countdown(n):
    if n == 0:
        return[]
    return [n] + countdown(n-1)
n = 5
print(countdown(n))