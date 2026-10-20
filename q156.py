class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def search_bst(root,val):
    current = root
    while current:
        if current.data == val:
            return True
        elif val < current.data:
            current = current.left
        else:
            current = current.right
    return False
#create the Bst
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
#search for values
print(search_bst(root,7))
print(search_bst(root,12))
print(search_bst(root,10))