class node:
    def __init__(self,data):
     self.data = data
     self.next = None
def get_value(head,k):
   current = head
   count = 0
   while current:
      if count == k:
         return current.data
      current = current.next
      count += 1
   return None
head = node(10)
head.next = node(20)
head.next.next = node(30)
head.next.next.next = node(40)
print(get_value(head,2)) 


