class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def is_valid_bst(root):
    def check(node, low, high):
        if node is None:
            return True
        if node.data <= low or node.data >= high:
            return False
        return (check(node.left, low, node.data) and check(node.right, node.data,high))
    return check(root,float("-inf"),float("inf"))
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print(is_valid_bst(root))