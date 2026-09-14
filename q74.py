def count_anagram_groups(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = 1
        else:
            groups[key] += 1
    count = 0
    for key in groups:
        if groups[key] > 1:
            count += 1
    return count
words = ["eat", "tea","tan","ate","nat","bat"]
print(count_anagram_groups(words))