#t14503_로봇청소기
from collections import deque
n, m = map(int,input().split())
r, c, d = map(int,input().split())
state=[]
for _ in range(n):
    state.append(list(map(int,input().split())))

#d 0 1 2 3 북 동 남 서 
dx = [-1,0,1,0]
dy = [0, 1, 0,-1]

visited = [[0]*m for _ in range(n)]
visited[r][c]=1
cnt=1
while True:
    flag = 0 #청소안함 
    for i in range(4):
        d = (d+3)%4
        nx = r + dx[d]#반시계방향으로 90도 회전 
        ny = c + dy[d]
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny]==0 and state[nx][ny]==0:
                visited[nx][ny]=1
                r = nx
                c = ny
                flag = 1
                cnt+=1
                break
                
    if flag == 0: #현재 칸의 주변4칸 중 청소되지 않은 빈칸이 없는 경우
        if state[r-dx[d]][c-dy[d]]==1: #후진했을때 벽이면
            print(cnt)
            break
        else:
            r=r-dx[d]
            c=c-dy[d] #후진하기 
                


