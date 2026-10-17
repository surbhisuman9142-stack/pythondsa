class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def right_view(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            if i == size - 1:
              result.append(node.data)
            if node.left:
             queue.append(node.left)
            if node.right:
             queue.append(node.right)
    return result
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(right_view(root))