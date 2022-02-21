#7569_토마토
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dx = [-1,1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                if graph[nx][ny][nz]==0:
                    q.append([nx,ny,nz])
                    graph[nx][ny][nz]=graph[x][y][z]+1


q=deque([])
M, N, H = map(int, sys.stdin.readline().split())
graph = []
path=[]
for h in range(H):
    graphtmp=[]
    for i in range(N):
        graphtmp.append(list(map(int,sys.stdin.readline().split())))
        for j in range(M):
            if graphtmp[i][j]==1:
                q.append([h,i,j])
    graph.append(graphtmp)
bfs()
    
res=0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        res = max(res, max(j))

print(res-1) 
