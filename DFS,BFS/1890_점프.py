#1890_점프
import sys
input = sys.stdin.readline

N = int(input())
game=[list(map(int,input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
visited[0][0]=1

for i in range(N):
    for j in range(N):
        if i==N-1 and j==N-1: #(N,N) 종착 
            print(visited[i][j])
            break
        cur = game[i][j]
        print(cur)
        if j+cur < N: #right
            visited[i][j+cur] += visited[i][j]
        if i+cur < N: #down
            visited[i+cur][j] += visited[i][j]
            
