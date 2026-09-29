class Node:
    def __init__(self,data):
     self.data = data
     self.next = None
def sum(Node):
   total = 0
   current = head
   while current :
      total += current.data
      current = current.next
   return total
head = None
current = None
for i in range(1,10):
   new_Node = Node(i)
   if head is None:
       head = new_Node
       current = head
   else:
      current.next = new_Node
      current = new_Node
print(sum(head))
      
   
        