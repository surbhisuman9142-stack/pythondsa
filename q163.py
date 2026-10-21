
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kth_smallest(root, k):
    values = []

    def inorder(node):
        if node is None:
            return

        inorder(node.left)
        values.append(node.data)
        inorder(node.right)

    inorder(root)

    if k < 1 or k > len(values):
        return None

    return values[k - 1]


# Create BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(kth_smallest(root, 1))
print(kth_smallest(root, 3))
print(kth_smallest(root, 5))
