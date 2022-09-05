#2178
from collections import deque
n, m = map(int, input().split())

miro = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    cnt=0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if miro[nx][ny]==1:
                    miro[nx][ny]=miro[x][y]+1
                    cnt+=1
                    q.append((nx,ny))
    return miro[n-1][m-1]

ans = bfs(0,0)

'''
for i in range(n):
    for j in range(m):
        if miro[i][j]==1:
            ans = dfs(i,j)
'''
print(ans)
