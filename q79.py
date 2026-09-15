class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def sum_values(head):
    total = 0
    current = head
    while current:
        total += current.data
        current = current.next
    return total
head = node(10)
head.next = node(20)
head.next.next = node(30)
print(sum_values(head))