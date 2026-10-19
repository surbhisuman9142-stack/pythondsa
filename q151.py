def next_number(nums):
    if len(nums) < 2 :
        return None
    #check arithmetic pattern
    difference = nums[1] - nums[0]
    arithmetic = True
    for i in range(1,len(nums) - 1):
        if nums[i + 1] - nums[i] != difference:
            arithmetic = False
        break
    if arithmetic:
        return nums[-1] + difference
    #check geometric pattern
    if nums[0] == 0:
        return None
    if nums[1] % nums[0] != 0:
        return None
    ratio = nums[1] // nums[0]
    for i in range(1,len(nums) - 1):
        if nums[i] * ratio != nums[i + 1]:
            return None
    return nums[-1] * ratio
print(next_number([2,4,6,8]))
print(next_number([3,6,12,24]))
print(next_number([1,4,9,16]))