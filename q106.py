from collections import deque
class RecentCounter:
    def __init__(self):
        self.queue = deque()
    def ping(self,t):
        self.queue.append(t)
        limit = t - 3000
        while self.queue[0] < limit:
            self.queue.popleft()
        return len(self.queue)
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))