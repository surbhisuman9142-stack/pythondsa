def permutations(nums):
    result = []
    def backtrack(current,remaining):
        if remaining == []:
            result.append(current)
            return
        for i in range(len(remaining)):
            num = remaining[i]
            backtrack(
            current + [num],
            remaining[:i] + remaining[i+1:]
           )
    backtrack([],nums)
    return result
nums = [1,2,3]
print(permutations(nums))