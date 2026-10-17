class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
def preorder(root):
    if root is None:
        return[]
    result = [root.val] + preorder(root.left) + preorder(root.right)
    return result
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Print pre-order traversal
print(preorder(root))
