def push_pop(xs):
    stack = []
    for x in xs:
        stack.append(x)
    result = []
    while stack:
        result.append(stack.pop())
    return result
print(push_pop([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]

