#15686_치킨배달
from collections import deque
from itertools import combinations
n, m = map(int,input().split())
city=[]
for _ in range(n):
    city.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
'''
def bfs(a,b):
    q = deque()
    q.append([a,b])
    visited = [[0]*(n) for _ in range(n)]
    distance = n+m
    tmp=[]
    cnt=0
    while q:
        cnt+=1
        x,y=q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if city[nx][ny]==2 and not visited[nx][ny]:#치킨집                  
                    distance = min(distance,abs(nx-x)+abs(ny-y))                  
                    tmp.append([nx,ny,abs(nx-a)+abs(ny-b)])
                    print("TMP",tmp)
                    print("city",city)
                    
                    visited[nx][ny]=1
                    print("visited",visited)
                    q.append([nx,ny])
                    print("q",q)
                    
                    if cnt>13:
                        break
        
    if len(tmp)>0:
        tmp.sort(key=lambda x:x[2])
        print("tmp",tmp)
        city[tmp[0][0]][tmp[0][1]]=0
 
    return [x, y, distance]
'''
house=[]
chicken=[]

for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            house.append([i,j])
        elif city[i][j]==2:
            chicken.append([i,j])
res=999999
for c in combinations(chicken, m):
    tmp=0
    for hx,hy in house:
        distance = m*n
        for j in range(m):
            distance = min(distance,abs(hx-c[j][0])+abs(hy-c[j][1]))
        
        tmp+=distance
    res = min(res, tmp)
print(res)
                         
#res.sort(key=lambda x: x[2])

#print(sum(i[2] for i in res[:m]))
