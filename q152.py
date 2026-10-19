def permutations_count(n):
    if n < 0:
        return None

    
    result = 1
    for i in range(1, n + 1):
        result = result * i

    return result
print(permutations_count(4))
print(permutations_count(5))
print(permutations_count(0))

