class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
def is_present(head,val):
    current = head
    while current:
        if current.data == val:
          return True
        else:
            current = current.next
head = Node(10)
head.next = Node(32)
head.next.next = Node(56)
val = 23
print(is_present(head,val))
