def asteriodcollision(asteriods):
    stack = []
    for asteriod in asteriods:
        while stack and asteriod < 0 and stack[-1] > 0:
            if stack[-1] < -asteriod:
                stack.pop()
            elif stack[-1] == -asteriod:
                stack.pop()
                break
            else:
                break
        else:
            stack.append(asteriod)
    return stack
asteriods = [5,10,-5]
print(asteriodcollision(asteriods))