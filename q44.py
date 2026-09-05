def count_even(list):
    count = 0
    for i in list:
        if i % 2 == 0:
            count += 1
    return count
list = [1, 2, 3, 4, 5]
print(count_even(list))