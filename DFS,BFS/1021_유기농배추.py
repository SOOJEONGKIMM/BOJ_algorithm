#1012_유기농배추
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

T=int(input())

def bfs(a,b,graph):
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
    return

for i in range(T):
    n,m,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y]=1
    res=0
    for a in range(n):
        for b in range(m):
            if graph[a][b]==1:
                bfs(a,b,graph)
                res+=1

    print(res)
    
