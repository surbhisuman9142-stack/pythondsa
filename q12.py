def count_vowels(str):
    vowels = set('aeiou')
    return sum(1 for c in str.lower() if c in vowels)
str = input("Enter a string:")
print(count_vowels(str))
