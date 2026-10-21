def two_sums(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return[seen[needed],i]
        seen[num] = i
    return []
print(two_sums([2,7,11,15],9))
print(two_sums([3,2,4],6))
print(two_sums([3,3],6))