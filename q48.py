def remove_val(a,val):
    slow = 0
    for x in a:
        if x != val:
            a[slow] = x
            slow += 1
    return slow
nums = [3, 2, 2, 3,2,4]
print(remove_val(nums, 3))