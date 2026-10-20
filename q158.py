class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def common_elements(list1, list2):
    common = []
    for num in list1:
        if num in list2 and num not in common:
              common.append(num)

    common.sort()
    return common
list1 = [4, 2, 1, 3, 2]
list2 = [3, 2, 5, 4]

print(common_elements(list1, list2))
    
    