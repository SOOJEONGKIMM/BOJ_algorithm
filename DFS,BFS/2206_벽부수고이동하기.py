#2206_벽부수고이동하기
from collections import deque


def bfs():
    visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0]=1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque([(0,0,0)])#좌표(행열),벽유무01
    while q:
        x, y, wall = q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][wall]
        for dis in range(4):
            nx = x + dx[dis]
            ny = y + dy[dis]
            if 0<=nx<n and 0<=ny<m:
                #벽 부수는 경우:
                if graph[nx][ny]==1 and wall==0:#벽이고 아직 안 부숨 
                    visited[nx][ny][1]=visited[x][y][0]+1
                    q.append([nx,ny,1])#벽 부숨 
                #벽이 아니고 방문안한 곳: 
                elif graph[nx][ny]==0 and visited[nx][ny][wall]==0:
                    visited[nx][ny][wall]= visited[x][y][wall]+1
                    q.append([nx,ny,wall])
    return -1
                
                    
n,m = map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
print(bfs())
