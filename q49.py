def pair_sum(a,target):
    i,j=0,len(a)-1
    while i<j:
        s = a[i]+a[j]
        if s==target:return(i,j)
        if s<target:i+=1
        else:j-=1
    return None
nums = [1,2,3,4,6]
print(pair_sum(nums, 6))