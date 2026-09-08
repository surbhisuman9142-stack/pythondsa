def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplet = [nums[i],nums[left],nums[right]]
                if triplet not in result:
                    result.append(triplet)
                left += 1
                right -= 1
            elif total < 0:
                left +=1
            else:
                right -= 1
    return result
nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))