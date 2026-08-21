def two_sum(numbers, target):
    seen =  {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return (seen[complement],i)
        seen[num] = i
    return None
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))