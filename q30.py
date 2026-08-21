def most_frequent(num):
    count = {}
    for item in num:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return max(count, key=count.get)
num = [1,2,2,3,2,4,3]
print(most_frequent(num))