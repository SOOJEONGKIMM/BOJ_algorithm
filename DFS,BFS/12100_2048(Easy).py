import sys
from copy import deepcopy

def move(board, dir):
    #print(board)
    if dir==0: #up
        for j in range(n):
            pointer = 0
            for i in range(1,n):
                #print(board[i][j])
                if board[i][j]:
                    tmp = board[i][j] #cur board num
                    board[i][j]=0
                    if board[pointer][j]==0:
                        board[pointer][j]=tmp
                    elif board[pointer][j]==tmp:
                        board[pointer][j]*=2
                        pointer+=1
                    else:
                        pointer+=1
                        board[pointer][j]=tmp
    if dir==1: #down
        for j in range(n):
            pointer = n-1
            for i in range(n-2,-1,-1):
                #n-1,n-2,n-3....0
                if board[i][j]:
                    tmp = board[i][j] #cur board num
                    board[i][j]=0
                    if board[pointer][j]==0:
                        board[pointer][j]=tmp
                    elif board[pointer][j]==tmp:
                        board[pointer][j]=tmp*2
                        pointer-=1
                    else:
                        pointer-=1
                        board[pointer][j]=tmp
    if dir==2: #right
        for i in range(n):
            pointer = n-1
            for j in range(n-2,-1,-1):
                if board[i][j]:
                    tmp = board[i][j] #cur board num
                    board[i][j]=0
                    if board[i][pointer]==0:
                        board[i][pointer]=tmp
                    elif board[i][pointer]==tmp:
                        board[i][pointer]=tmp*2
                        pointer-=1
                    else:
                        pointer-=1
                        board[i][pointer]=tmp
    if dir==3: #left
        for i in range(n):
            pointer = 0
            for j in range(1,n):
                if board[i][j]:
                    tmp = board[i][j] #cur board num
                    board[i][j]=0
                    if board[i][pointer]==0:
                        board[i][pointer]=tmp
                    elif board[i][pointer]==tmp:
                        board[i][pointer]=tmp*2
                        pointer+=1
                    else:
                        pointer+=1
                        board[i][pointer]=tmp
    return board

def dfs(board, cnt):
    global ans
    if cnt==5:
        for i in range(n):
            for j in range(n):
                ans=max(ans,board[i][j])
        return
    for i in range(4):
        #print("here",board,i)
        tmp_board = move(deepcopy(board),i)
        dfs(tmp_board, cnt+1)

n = int(input())
graph = list(list(map(int,input().split())) for _ in range(n))

ans = 0 
dfs(graph, 0)
print(ans)
