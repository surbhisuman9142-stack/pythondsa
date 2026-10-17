class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def search_tree(root,val):
    if root is None:
        return False
    if root.data == val:
        return True
    return search_tree(root.left, val) or search_tree(root.right, val)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

print(search_tree(root, 10))
print(search_tree(root, 50))