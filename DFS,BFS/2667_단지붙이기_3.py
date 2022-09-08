#2667
from collections import deque
n=int(input())
danzi = [list(map(int, input())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y,k):
    q=deque()
    q.append((x,y))
    danzi[x][y]=0
    d=0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if danzi[nx][ny]!=0 and danzi[nx][ny]==k:
                    q.append((nx,ny))
                    d+=1
                    danzi[nx][ny]=0
    return d+1

dd=[]
for i in range(n):
    for j in range(n):
        if danzi[i][j]!=0:
            dd.append(bfs(i,j,danzi[i][j]))

print(len(dd))
dd.sort()
for a in dd:
    print(a)
