def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
        return result
num = [4, 1, 2, 1, 2]
print(single_number(num))
