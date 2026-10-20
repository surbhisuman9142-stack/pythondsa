class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def anagram_key(word):
    return "".join(sorted(word))
word = "listen"
print(anagram_key(word))

