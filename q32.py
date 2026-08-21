from  collections import Counter
def word_freq(text):
    return dict(Counter(text.lower().split()))
text = "hello world"
print(word_freq(text))
                