def top_k_frequent(nums,k):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    sorted_nums = sorted(freq, key=freq.get,reverse=True)
    return sorted_nums[:k]
nums = [1,1,2,2,2,3]
k = 2
print(top_k_frequent(nums,k))
