def frequency_sort(s):
    count ={}
    for ch in s:
        count[ch] = count.get(ch,0) + 1
    result = ""
    while count:
        max_char = max(count, key=count.get)
        result += max_char * count[max_char]
        del count[max_char]
    return result
s = "tree"
print(frequency_sort(s))