class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def add_two_numbers(head1,head2):
    dummy = Node(0)
    current = dummy
    carry = 0
    while head1 is not None and head2 is not None or carry != 0:
        if head1 is not None:
            value1 = head1.data
        else:
            value1 = 0

        if head2 is not None:
            value2 = head2.data
        else:
            value2 = 0
        total = value1 + value2 + carry
        digit = total % 10
        carry =total // 10
        current.next = Node(digit)
        current = current.next
        if head1 is not None:
            head1 = head1.next
        if head2 is not None:
            head2 = head2.next
    return dummy.next
head1 = Node(2)
head1.next = Node(4)
head1.next.next = Node(3)

head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(4)

result = add_two_numbers(head1, head2)

current = result

while current is not None:
    print(current.data, end="->")
    current = current.next

print("None")
