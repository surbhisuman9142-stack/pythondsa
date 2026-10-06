def flatten(numbers):
    result = []
    for item in numbers:
        if isinstance(item,list):
            result += flatten(item)
        else:
            result.append(item)
    return result
numbers = [1,[2,3],[4,[5,6]],7]
print(flatten(numbers)) 