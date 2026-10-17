class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def sum_nodes(root):
    if root is None:
        return 0
    left_sum = sum_nodes(root.left)
    right_sum = sum_nodes(root.right)
    return root.data + left_sum + right_sum

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(sum_nodes(root))
