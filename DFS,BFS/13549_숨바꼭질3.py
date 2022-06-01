#13549_숨바꼭질3
from collections import deque
n, k= map(int,input().split())

q=deque()
q.append(n)
visited=[-1 for _ in range(100001)]
visited[n]=0
while q:
    cur = q.popleft()
    if cur==k:
        print(visited[cur])
        break
    if 0<=cur-1<=100000 and visited[cur-1]==-1:
        visited[cur-1]=visited[cur]+1
        
        q.append(cur-1)
    if 0<cur*2<=100000 and visited[cur*2]==-1:
        visited[cur*2]=visited[cur]
        
        q.appendleft(cur*2)
    
    if 0<=cur+1<=100000 and visited[cur+1]==-1:
        visited[cur+1]=visited[cur]+1
        q.append(cur+1)


