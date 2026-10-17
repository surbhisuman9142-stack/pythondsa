class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirror(root):
    if root is None:
        return None

    # Swap left and right children
    root.left, root.right = root.right, root.left

    mirror(root.left)
    mirror(root.right)

    return root


def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Before mirroring:")
preorder(root)

