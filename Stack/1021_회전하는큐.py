#1021_회전하는큐
from collections import deque
n,m=map(int,input().split())
q = deque([i for i in range(1,n+1)])
popping = list(map(int,input().split()))
j=0
ans=0

for i in range(m):
    findindex = q.index(popping[i])
    if findindex < len(q) - findindex:
        while True:
            #print(q)
            tmp=q.popleft()
            if tmp==popping[i]:
                break
            else:
                q.append(tmp)
                ans+=1
            
    else:
        while True:
            #print(q)
            tmp=q[0]
            if tmp==popping[i]:
                q.popleft()
                break
            else:
                q.appendleft(q.pop())
                ans+=1
           

print(ans)
