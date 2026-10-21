def contains_nearby_duplicate(nums,k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen:
            if i - seen[num] <= k:
               return True
        seen[num] = i
    return False
print(contains_nearby_duplicate([1,2,3,1],3))
print(contains_nearby_duplicate([1,2,3,1],2))