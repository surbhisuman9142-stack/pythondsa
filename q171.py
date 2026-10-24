class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def range_sum_bst(root,low,high):
    if root is None:
        return 0
    if root.data < low:
        return range_sum_bst(root.right, low, high)
    if root.data > high:
        return range_sum_bst(root.left, low, high)
    return (root.data + range_sum_bst(root.left, low, high) + range_sum_bst(root.right,low,high))
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

# Set the range
low = 5
high = 15

# Print the result
print(range_sum_bst(root, low, high))