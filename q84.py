class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def append(head, val):
    new_Node = Node(val)

    if head == None:
        head = new_Node
        return head

    current = head

    while current.next != None:
        current = current.next

    current.next = new_Node

    return head


head = Node(20)
head.next = Node(30)

head = append(head, 40)

current = head

while current:
    print(current.data)
    current = current.next