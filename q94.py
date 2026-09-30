class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def is_palindrome(head):
    values  = []
    current = head
    while current is not None:
        values.append(current.data)
        current = current.next
        left = 0
        right = len(values) - 1
        while left < right :
            if values[left] != right:
                return False
            left += 1
            right -= 1
        return True
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
print(is_palindrome(head))