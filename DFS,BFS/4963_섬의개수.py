#4963_섬의개수
import sys
from collections import deque 
input = sys.stdin.readline

#direction in mapp
dx = [1,-1,0,0,1,-1,1,-1] #right, left, up, down, diag(") 
dy = [0,0,-1,1,-1,1,1,-1]

def bfs(x,y):
    mapp[x][y]=0
    q=deque()
    q.append([x,y])
    while q:
        a,b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and mapp[nx][ny]==1:
                mapp[nx][ny]=0
                q.append([nx,ny])


while(1):
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    mapp = []
    cnt=0
    for _ in range(h):
        mapp.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if mapp[i][j] == 1:
                bfs(i,j)
                cnt+=1

    print(cnt)
