class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def mirror(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)
    return root
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root = mirror(root)
def preorder(root):
    if root is None:
        return []
    return [root.data] + preorder(root.left) + preorder(root.right)
print(preorder(root))