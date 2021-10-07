#18428_감시피하기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
hallway = [list(map(str, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
q=deque()
def bfs():
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if hallway[i][j] == 'T':
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for i in range(4):
            temp_x, temp_y = x, y
            while (1):                    
                nx,ny = dx[i]+temp_x, dy[i]+temp_y
                if 0<= nx < N and 0<= ny < N:
                    if hallway[nx][ny]=="X" and visited[nx][ny] == 0:
                        visited[nx][ny]=1                   
                    elif hallway[nx][ny]=="S":
                        return False

                    elif hallway[nx][ny]=="O":
                        break
                    temp_x, temp_y = nx, ny
                else:
                    break
    return True
                
                    
flag = False
loop_cnt=0
backup_hall=hallway
def search(k):
    global flag
    if k==3:
        if bfs():
            flag = True
        return
    for i in  range(N):
        for j in range(N):
            
            if hallway[i][j]=="X":
                hallway[i][j]="O"
                search(k+1)
                hallway[i][j]="X"

                
search(0)       
if flag:
    print("YES")
elif flag==False:
    print("NO")



    
