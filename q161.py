class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def first_repeated(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None
print(first_repeated([1,2,3,2,1]))
print(first_repeated([4,5,6]))
print(first_repeated([1,3,1,3]))