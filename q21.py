def max(list):
    max_value = list[0]
    for i in range(len(list)):
       if list[i] > max_value:
         max_value = list[i]
    return max_value
list = [1,4,6,8,9]
print(max(list))