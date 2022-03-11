#11657_타임머신
import sys
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans=0
def dfs(x,y,cnt):
    global ans
    ans=max(ans, cnt)

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0<=tx<r and 0<=ty<r and visited[ord(a[tx][ty])-65]!=1:
            visited[ord(a[tx][ty])-65]=1
            ncnt = cnt+1
            dfs(tx,ty,ncnt)
            visited[ord(a[tx][ty])-65]=0
            
r,c = map(int, sys.stdin.readline().split())
a=[]
for _ in range(r):
    a.append(sys.stdin.readline())
visited = [0]*26
visited[ord(a[0][0])-65]=1
dfs(0,0,1)
print(ans)
