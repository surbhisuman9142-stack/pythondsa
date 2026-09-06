def is_palinrome(nums):
    left = 0
    right = len(nums)-1
    while left<right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    return True
nums = [1,2,3,2,1]
print(is_palinrome(nums))