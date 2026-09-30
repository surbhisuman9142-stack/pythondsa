class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head.next
visited = set()
current = head
while current:
    if current in visited:
        print(True)
        break
    visited.add(current)
    current = current.next
else:
    print(False)
