def first_unique (nums):
    for num in nums:
        if nums.count(num) == 1:
            return num
    return None
nums = [4,5,1,4,5,2]
print(first_unique(nums))
