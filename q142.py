class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def serialize(root):
    values = []
    def preorder(node):
        if node is None:
            values.append("#")
            return
        values.append(str(node.data))
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return ",".join(values)
def deserialize(data):
    values = iter(data.split(","))
    def build():
        value = next(values)
        if value == "#":
         return None
        node = Node(int(value))
        node.left = build()
        node.right = build()
        return node
    return build()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
encoded = serialize(root)
print("Encoded:", encoded)
new_root = deserialize(encoded)
print("Decode and encoded again:", serialize(new_root))
