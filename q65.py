def is_palindrome(s):
    result = ""
    for ch in s:
        if ch.isalnum():
            result +=ch.lower()
    return result == result[::-1]
s = "A man, a"
print(is_palindrome(s))