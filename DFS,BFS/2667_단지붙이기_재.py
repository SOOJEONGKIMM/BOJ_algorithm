#2667_단지번호붙이기
from collections import deque
n=int(input())
danzi=[]
for _ in range(n):
    danzi.append(list(map(int,input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(danzi, x, y):
    queue=deque([])
    queue.append([x,y])
    danzi[x][y]=0
    cnt=1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if danzi[nx][ny]==1:
                    danzi[nx][ny]=0
                    cnt+=1
                    queue.append([nx,ny])
    return cnt

res=[]
for i in range(n):
    for j in range(n):
        if danzi[i][j]==1:
            res.append(bfs(danzi,i,j))

print(len(res))
for i in res:
    print(i)
