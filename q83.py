class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def get_value(head,k):
 current = head
 index = 0
 while current:
   if index == k:
      return current.data
   current = current.next
   index += 1
 return None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
k = 2
print(get_value(head,k))
     
