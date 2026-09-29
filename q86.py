class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def max(head):
    max = head.data
    current = head
    while current:
       if current.data > max:
           max = current.data
       current = current.next
    return max
head = Node(5)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(2)
print(max(head))


