class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    result = []
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        result.append(node.data)
        traverse(node.right)
    traverse(root)
    return result
root = Node(2)
root.left = Node(1)
root.right = Node(3)
print(inorder(root))
