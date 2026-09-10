def sort_words(words):
    words.sort(key=lambda word:(len(word), word))
    return words
words = ["cat" ,"apple","dog","bat","hi"]
print(sort_words(words))