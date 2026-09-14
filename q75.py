def longest_palindrome(s):
    if len(s) <= 1:
        return s
    longest = ""
    for i in range(len(s)):
        left = i
        right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(longest):
                longest = s[left:right + 1]
            left -= 1
            right += 1
        left = i
        right = i + 1
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left + 1 > (longest):
            longest = s[left:right + 1]
        left -= 1
        right += 1
    return longest
s = "babd"
print(longest_palindrome(s))