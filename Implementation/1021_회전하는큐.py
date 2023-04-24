#1021_회전하는 큐
import sys
from collections import deque
n, m = map(int,input().split())
place = list(map(int,input().split()))
q = deque([i for i in range(1,n+1)])
ans = 0

for i in range(m):
    
    findindex = q.index(place[i])
    if findindex < len(q) - findindex:
        while True:
            tmp = q.popleft()
            if tmp==place[i]:
                break
            else:
                q.append(tmp)
                ans+=1
    else:
        while True:
            tmp = q[0]
            if tmp==place[i]:
                q.popleft()
                break
            else:
                
                right = q.pop()
                q.appendleft(right)
                ans+=1

print(ans)
