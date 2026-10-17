class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def has_path_sum(root,target):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.data == target
    remaining = target - root.data
    return(has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining))
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.right.left = Node(13)
root.right.right = Node(4)

root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.right.right = Node(1)

target = 20

print(has_path_sum(root, target))