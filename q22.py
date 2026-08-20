def unique_count(list):
    unique_num = set(list)
    return len(unique_num)
list = [1,1,2,3,4,5,5]
print(unique_count(list))