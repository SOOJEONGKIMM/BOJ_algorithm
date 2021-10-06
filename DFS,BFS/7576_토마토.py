#7576_토마토
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < M:
                if graph[nx][ny]==0:
                    q.append([nx,ny])
                    graph[nx][ny]=graph[x][y]+1


        

q=deque([])
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
path = []
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            q.append([i,j])
            
bfs()
res=0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res-1)
