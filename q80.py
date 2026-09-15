class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print(length(head))