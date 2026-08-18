total = int(input("Enter total seconds:"))
hours = total // 3600
minutes = (total % 3600) // 60
seconds = total % 60
print( hours, ":", minutes,":" ,seconds)



