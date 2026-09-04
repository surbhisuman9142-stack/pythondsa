def group_Anagram(strs):
    Anagram = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in Anagram:
            Anagram[key] = []
        Anagram[key] .append(word)
    return list(Anagram.values())
strs = ["eat", "bat" , "tea", "ate", "atb","ten"]
print(group_Anagram(strs))

