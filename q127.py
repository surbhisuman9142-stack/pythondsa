class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def count_nodes(root):
    if root is None:
        return 0
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    return 1 + left_count + right_count
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(count_nodes(root))