from copy import deepcopy
dx=[0,0,1,-1]
dy=[1,-1,0,0]

scan=[[[0],[1],[2],[3]],
      [[0,1],[2,3]],
      [[0,3],[1,3],[1,2],[0,2]],
      [[0,1,3],[1,2,3],[0,1,2],[0,2,3]]
      ]

N,M=map(int,input().split())

room=[]
tv=[]
all=[]
def dfs(depth):
    global answer,watch
    if depth==t_len:
        ha=0
        for x in range(N):
            ha+=watch[x].count(0)

        answer=min(answer,ha)
        return
    tx,ty,num=tv[depth]
    now_scan=scan[num]
    temp=deepcopy(watch)
    for case in now_scan:
        for do in case:
            nx=tx
            ny=ty
            while True:
                nx += dx[do]
                ny += dy[do]
                if not inside(nx, ny):
                    break
                if room[nx][ny] == 6:
                    break
                watch[nx][ny] = 1

        dfs(depth+1)
        watch=deepcopy(temp)

def inside(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False

    return True



watch=[[0]*M for _ in range(N)]
for i in range(N):
    tmp=list(map(int,input().split()))
    room.append(tmp)
    for j in range(M):
        if 1<=tmp[j]<=4:
            tv.append((i,j,tmp[j]-1))
            watch[i][j]=1
        elif tmp[j]==5:
            all.append((i,j))
            watch[i][j]=1
        elif tmp[j]==6:
            watch[i][j]=1
t_len=len(tv)

answer=1e9


#먼저, 전방위로 스캔하는 거 먼저.
#탐색 최소화

for x,y in all:
    for d in range(4):
        nx=x
        ny=y

        while True:
            nx+=dx[d]
            ny+=dy[d]
            if not inside(nx,ny):
                break
            if room[nx][ny]==6:
                break
            watch[nx][ny]=1


dfs(0)
print(answer)
