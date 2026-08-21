def remove_duplicates(list):
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result
list = [4,4,5,6,6,7,8,1,1,]
print(remove_duplicates(list))