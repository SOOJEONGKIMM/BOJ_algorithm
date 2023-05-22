#11657_타임머신
import sys
dx=(-1,1,0,0)
dy=(0,0,-1,1)
ans=0

def dfs(x,y,cnt):
    global ans
    ans=max(ans, cnt)

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0<=tx<r and 0<=ty<c and not a[tx][ty] in alphas:
            alphas.add(a[tx][ty])
            ncnt = cnt+1
            dfs(tx,ty,ncnt)
            alphas.remove(a[tx][ty])
            
r,c = map(int, sys.stdin.readline().split())
a=[]
for _ in range(r):
    a.append(list(map(lambda x:ord(x)-65, sys.stdin.readline().rstrip())))
#print(a)
#visited = [0]*26
alphas=set()
alphas.add(a[0][0])
#visited[a[0][0]]=1
dfs(0,0,1)
print(ans)
