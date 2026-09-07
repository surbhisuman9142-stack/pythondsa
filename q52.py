def merge(list1,list2):
    result = list1 + list2
    result.sort()
    return result
list1 = [1,3,5,7]
list2 = [2,4,6,8]
print(merge(list1,list2))
    