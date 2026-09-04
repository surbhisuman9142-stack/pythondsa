def first_unique(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num in nums:
        if count[num] == 1:
            return num
    return None
nums = [4,5,1,4,5,2]
print(first_unique(nums))