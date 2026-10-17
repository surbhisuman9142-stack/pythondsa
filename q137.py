class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def is_same(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return is_same(root1.left, root2.left) and is_same(root1.right,root2.right)
root1 = Node(2)
root1.left = Node(1)
root1.right = Node(3)


root2 = Node(2)
root2.left = Node(1)
root2.right = Node(3)

print(is_same(root1, root2))

