#10026_적록색약
import sys
from collections import deque 
read = sys.stdin.readline

n=int(read())

colors = [list(read().rstrip()) for _ in range(n)]



q=deque()

def bfs(x,y):
    q.append((x,y))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    visited[x][y]=1

    while q:
        x,y=q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and colors[nx][ny]==colors[x][y]:
                visited[nx][ny]=1
                q.append((nx,ny))
cnt_rgb=0
visited = [[0] * n for _ in range(n)]           
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt_rgb+=1

for i in range(n):
    for j in range(n):
        if colors[i][j]=='G':#G 모두 R로 바꾸
            colors[i][j]='R'

cnt_rb=0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt_rb+=1

print(cnt_rgb, cnt_rb)



