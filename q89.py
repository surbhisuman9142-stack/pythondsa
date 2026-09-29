class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def middle(head):
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
    middle_index = count // 2
    current = head
    for i in range(middle_index):
        current = current.next
    return current.data
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print(middle(head))