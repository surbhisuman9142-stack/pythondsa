def sum_list(numbers):
    if numbers == []:
        return 0
    return numbers[0] + sum_list(numbers[1:])
numbers = [1,2,3,4]
print(sum_list(numbers))
 