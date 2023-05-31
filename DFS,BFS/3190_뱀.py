#3190_뱀
from collections import deque
N=int(input())
K=int(input())

board = [[0]*N for _ in range(N)]

for _ in range(K):
    row, col = map(int,input().split())
    board[row-1][col-1]=1#사과 


L=int(input())
snake = dict()
for _ in range(L):
    X, C = map(str,input().split())
    
    snake[int(X)]=C
q=deque()
q.append([0,0])
board[0][0]=2#뱀 
direction=0
def turn(alpha):
    global direction
    if alpha=="L":
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
        
dx=[0,1,0,-1] #오른쪽부터 
dy=[1,0,-1,0]

x,y=0,0
cnt=0

while True:
    cnt+=1
    x+=dx[direction]
    y+=dy[direction]
    if x<0 or x>N-1 or y<0 or y>N-1:
        
        break
    
    if board[x][y]==1:#사과
        board[x][y]=2
        q.append([x,y])
        if cnt in snake:
            turn(snake[cnt])
    elif board[x][y]==0:#빈칸 
        board[x][y]=2
        q.append([x,y])
        tx,ty = q.popleft()
              
        board[tx][ty]=0
        if cnt in snake:
            turn(snake[cnt])
    else:
        break

print(cnt)            
                
                
            

