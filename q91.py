class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def delete_node(head,val):
    dummy = Node(0)
    dummy.next = head
    current = dummy
    while current.next:
        if current.next.data == val:
            current.next = current.next.next
            break
        current = current.next
        return dummy.next
head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head = delete_node(head,20)
current = head
while current:
  print(current.data, end="-> ")
  current = current.next
print("None")


