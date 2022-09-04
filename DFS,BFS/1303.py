import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

col=[list(sys.stdin.readline().strip()) for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y,c):
    q = deque()
    q.append((x,y))
    cnt = 0 
    while q:
	x, y = q.popleft()
	for i in range(4):
	    nx = x + dx[i]
	    ny = y + dy[i]
	    if 0<=nx<m and 0<ny<n:
		if col[nx][ny]==c and col[nx][ny]!=0:
		    q.append((nx,ny))
		    cnt+=1
		    col[nx][ny]=0
    return (1 if cnt==0 else cnt)		   

w_cnt, b_cnt = 0, 0

for i in range(m):
    for j in range(n):
	if col[i][j]!=0:
	    if col[i][j]=='W':
		w_cnt += bfs(i,j,col[i][j])**2
	    elif col[i][j]=='B':
		b_cnt += bfs(i,j,col[i][j])**2
    
print(w_cnt, b_cnt)
