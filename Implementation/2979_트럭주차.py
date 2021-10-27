#2979_트럭주차
A, B, C = map(int, input().split())

arr=[list(map(int, input().split())) for _ in range(3)]

n = max(arr[0][1],arr[1][1],arr[2][1])
board = [0]*(n-1)
for i in arr:
    for j in range(i[0]-1,i[1]-1):
        board[j]+=1
fee=0
for i in board:
    if i==1:
        fee += A
    elif i==2:
        fee += 2*B
    elif i==3:
        fee += 3*C
print(fee)
    
