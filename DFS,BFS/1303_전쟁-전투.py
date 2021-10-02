#1303_전쟁-전투
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

## W or B?
def bfs(x,y,col):
    q = deque()
    q.append((x,y))
    cnt=0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):#상하좌우 병사 탐색 
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <=ny < N:
                if color[nx][ny] == col and color[nx][ny]!=0:
                    q.append((nx,ny))
                    cnt+=1
                    color[nx][ny]=0
                    
    return (1 if cnt==0 else cnt)
    


N, M = map(int, input().split())

color = [list(input().strip()) for _ in range(M)]


w_cnt, b_cnt=0,0
for i in range(M):
    for j in range(N):
        if color[i][j]!=0:
            if color[i][j]=='W':
                w_cnt += bfs(i,j,color[i][j])**2
            elif color[i][j]=='B':
                b_cnt += bfs(i,j,color[i][j])**2
            
print(w_cnt, b_cnt)
