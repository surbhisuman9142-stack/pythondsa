def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 40:
        return 'C'
    else:
        return "Fail"
score  = int(input("Enter your score:"))
print (grade(score))
    