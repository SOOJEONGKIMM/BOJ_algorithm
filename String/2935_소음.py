#2935_소음
board=[]
for i in range(3):
    board.append(input())

a=int(board[0])
b=board[1]
c=int(board[2])
if b=='*':
    print(a*c)
elif b=='+':
    print(a+c)
