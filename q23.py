def has_duplicate(list):
    if len(list) != len(set(list)):
        return True
    else:
        return False
list = [1,2,3,4]
print(has_duplicate(list))