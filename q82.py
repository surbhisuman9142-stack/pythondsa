class Node:
      def __init__(self,data):
            self.data = data
            self.next = None 
def length(head):
     count = 0
     current = head
     while current:
           count += 1
           current = current.next
     return count
head = None
current = None
for i in range(0,50):
       new_Node = Node(i)
       if head is None:
            head = new_Node
            current = head
       else:
            current.next = new_Node
            current = new_Node
print(length(head)) 