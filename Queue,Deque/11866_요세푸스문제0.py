#11866_요세푸스문제
from collections import deque
n,k =map(int,input().split())
queue=deque([])
for i in range(1,n+1):
    queue.append(i)

print("<",end='')

while queue:
    for i in range(k-1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(),end='')
    if queue:
        print(', ',end='')

print('>')
        
