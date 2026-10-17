from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(level_order(root))