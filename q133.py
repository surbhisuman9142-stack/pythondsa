class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if root is None:
        return[]
    result = inorder(root.left) + [root.data] + inorder(root.right)
    return result
root = Node(2)
root.left = Node(1)
root.right = Node(3)

print(inorder(root))