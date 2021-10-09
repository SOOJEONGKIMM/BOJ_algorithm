#2583_영역 구하기
import sys
from collections import deque
input = sys.stdin.readline
M, N, K = map(int, input().split())
#M:세로, N:가로 (상하반전) 
dy = [-1,1,0,0]
dx = [0,0,-1,1]
graph = [list([0]*N) for _ in range(M)]

def bfs(x,y):
    cnt =1
    q=deque([])
    q.append([x,y])
    graph[i][j]=1

    while q:
        y,x=q.popleft()
        for k in range(4):
            nx , ny = x+dx[k], y+dy[k]
            if 0<= nx < N and 0<= ny < M:
                if graph[ny][nx]==0:
                    graph[ny][nx]=1
                    q.append([ny,nx])
                    cnt += 1
    return cnt
    

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=-1

res_cnt = []
for i in range(M): 
    for j in range(N):
        if graph[i][j]==0:
            res_cnt.append(bfs(i,j))

res_cnt.sort()
print(len(res_cnt))
for i in res_cnt:
    print(i, end=" ")

        
