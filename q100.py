xs = [10,20,30,40]
from collections import deque
q = deque()
for x in xs:
    q.append(x)
result = []
while q:
    result.append(q.popleft())
print(result)  
    