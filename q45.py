def adjacent_sums(nums):
    result = []
    for i in range(len(nums) - 1):
        result.append(nums[i] + nums[i + 1])
    return result
nums = [1, 2, 3, 4, 5]
print(adjacent_sums(nums))