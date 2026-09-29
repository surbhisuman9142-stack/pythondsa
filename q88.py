class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    previous = None
    current = head

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head = reverse(head)

current = head
while current:
    print(current.data)
    current = current.next