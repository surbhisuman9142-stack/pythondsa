class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def bst_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.data
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
print(bst_min(root))