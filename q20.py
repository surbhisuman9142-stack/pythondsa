def sum(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total
list = [1,2,3,4,5]
print(sum(list))