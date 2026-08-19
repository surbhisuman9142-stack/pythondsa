n = int(input("Enter any number: "))

result = 0

while n > 0:
    digit = n % 10
    result = result + digit
    n = n // 10

print("Sum =", result)