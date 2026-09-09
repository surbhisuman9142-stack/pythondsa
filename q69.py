def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped = True
        if not swapped:
                break
    return nums
nums = [5,2,4,1,3]
print(bubble_sort(nums))