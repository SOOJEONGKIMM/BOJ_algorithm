
#16234_인구이동
from collections import deque
n, l, r = map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(a,b):
    q = deque([(a,b)])
    tmp = [[a,b]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if l<=abs(graph[nx][ny]-graph[x][y])<=r:
                    visited[nx][ny]=1
                    q.append([nx,ny])
                    tmp.append([nx,ny])


    return tmp

res=0
while True:
    visited = [[0]*(n+1) for _ in range(n+1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j]=1
                country = bfs(i,j)
                if len(country)>1:
                    flag=1
                    num = sum([graph[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        graph[x][y]=num
                

    if flag==0:
        break
    res+=1

print(res)
    
