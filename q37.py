def top_k_frequent(nums,k):
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1
    result = sorted(count, key = count.get, reverse = True)
    return result[:k]
nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums,k))
        