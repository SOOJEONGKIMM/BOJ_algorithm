#13460_구슬탈출2
import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
s=[]
for i in range(n):
    a = list(input())
    s.append(a)
    for j in range(m):
        if a[j]=="R":
            ri,rj=i,j
        if a[j]=="B":
            bi,bj=i,j
q=deque()
q.append([ri,rj,bi,bj,1])


#bfs
dx = [1,-1,0,0]
dy = [0,0,-1,1]
visit = [[[[-1]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visit[ri][rj][bi][bj]=1

def move(i,j,dx,dy):
    c=0
    while s[i+dx][j+dy]!="#" and s[i][j]!="O":
        i+=dx
        j+=dy
        c+=1
    return i,j,c

def bfs():
    while q:
        ri,rj,bi,bj,d = q.popleft() #d는 이동횟수 
        if d>10:
            break
        for i in range(4):
            nri, nrj, rc = move(ri,rj, dx[i],dy[i])
            nbi, nbj, bc = move(bi,bj, dx[i],dy[i])
            if s[nbi][nbj]!="O":
                if s[nri][nrj]=="O":
                    print(d)
                    return
                if nri==nbi and nrj==nbj:#r이랑 b가 겹칠때 
                    if rc>bc:
                        nri-=dx[i]
                        nrj-=dy[i]
                    else:
                        nbi-=dx[i]
                        nbj-=dy[i]

                if visit[nri][nrj][nbi][nbj]==-1:
                    visit[nri][nrj][nbi][nbj]=1
                    q.append([nri,nrj,nbi,nbj,d+1])

    print(-1)

bfs()             
