def top(stack):
    if len(stack) == 0:
        return None
    return  stack[-1]
print(top([1,2,3,4,5]))
