class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def remove_node(head,n):
    dummy = Node(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    for i in range(n):
        fast = fast.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head = remove_node(head,2)
current = head
while current is not None:
    print(current.data, end= "->")
    current = current.next
print("None")
