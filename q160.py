class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def count_values(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts
nums = [1,2,2,3,1,2,4]
print(count_values(nums))
    