class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def lca(root, p ,q):
    if root is None:
        return None
    if root.data == p or root.data == q:
        return root
    left = lca(root.left,p,q)
    right = lca(root.right,p,q)
    if left and right:
        return root
    if left:
        return left
    return right
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
p = 4
q = 5
answer = lca(root,p,q)
if answer:
    print(answer.data)
else:
    print(None)