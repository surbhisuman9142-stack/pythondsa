def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
list = [1, 2, 3, 4, 5]
print(max(list))