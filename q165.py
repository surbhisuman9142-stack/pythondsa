def intersection(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    result = set()
    for num in list1:
        if num in set2:
            result.add(num)
    return list(result)
list1 =  [1, 2, 2, 3, 4]
list2 = [2, 3, 3, 5]

print(intersection(list1, list2))