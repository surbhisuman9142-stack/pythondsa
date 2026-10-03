class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self,x):
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        elif x < self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])
    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def get_min(self):
        return self.min_stack[-1]
s = MinStack()
s.push(5)
s.push(2)
s.push(8)
s.push(1)
print(s.stack)
print(s.min_stack)
print(s.top())
print(s.get_min())
print(s.pop())
print(s.get_min())