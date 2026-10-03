class MyQueue:
    def __init__(self):
        self.stack1 =[]
        self.stack2 = []
    def push(self,x):
        self.stack1.append(x)
    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.pop())
q.push(40)
print(q.pop())
    