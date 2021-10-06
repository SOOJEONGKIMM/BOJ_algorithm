#2468_안전 영역
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

cur_max = 0
for i in range(N):
    for j in range(N):
        cur_max = max(cur_max, graph[i][j])
     
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt=0
def bfs(x,y,k):
    cnt=1
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        visited[x][y]=1
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0<= nx < N and 0<= ny < N:
                if graph[nx][ny]>k and visited[nx][ny]==0:
                    q.append((nx,ny))
                    cnt+=1
                    visited[nx][ny]=1
                   
    return cnt 

res=0
for k in range(cur_max+1):
    visited = [[0]*N for _ in range(N)]
    res_cnt=[]
    for i in range(N):
        for j in range(N):
            if graph[i][j]>k and visited[i][j]==0:
                res_cnt.append(bfs(i,j,k))
                cnt=0
    res = max(res, len(res_cnt))

print(res)
