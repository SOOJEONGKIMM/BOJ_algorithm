#2636_치즈
from collections import deque
m, n = map(int,input().split())
cheeze_map=[]
for _ in range(m):
    cheeze_map.append(list(map(int,input().split())))


#bfs
def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(0,0)])
    melt = deque([]) #치즈 넣을 곳 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    if cheeze_map[nx][ny]==0:
                        q.append([nx, ny])
                    else:
                        melt.append([nx,ny])

    for x, y in melt:
        cheeze_map[x][y]=0 #치즈 다 녹임 
    return len(melt)
melt_cnt=[]
cnt=0
while True:
    visited = [[0]*n for _ in range(m)]
    cnt = bfs()
   
    if cnt==0:
        break
    melt_cnt.append(cnt)
print(len(melt_cnt))
print(melt_cnt[-1])
    
    
