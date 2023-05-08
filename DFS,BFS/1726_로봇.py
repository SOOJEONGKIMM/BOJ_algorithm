#1726_로봇
from collections import deque
def bfs():
    #global cnt
    visited=[[[0]*4 for _ in range(n)] for _ in range(m)]
    dc = [1,-1,0,0]
    dr = [0,0,1,-1]
    change_dir = [[2,3],[2,3],[0,1],[0,1]]#동서 동서 남북 남북 
    visited[sr-1][sc-1][sd-1]=1
    q = deque([(sr-1,sc-1,sd-1,0)])
    while q:
        
        r, c, d, cnt = q.popleft()
       
        if r==ar-1 and c==ac-1 and d==ad-1:#목적지 도착 
            return cnt

        
        #좌표 이동 
        for dis in range(1,4):
            nr = r + dr[d] * dis
            nc = c + dc[d] * dis
            nd = d
            if not (0<=nr<m and 0<=nc<n) or rect[nr][nc]:#맵을 벗어나거나 벽 부딪히면 
                break
            if visited[nr][nc][nd]:
                continue
            
            q.append((nr,nc,nd,cnt+1))
            visited[nr][nc][nd]=1
            
        #방향 바꾸기
        for nd in change_dir[d]:
            if visited[r][c][nd]:
                continue
            
            q.append((r,c,nd,cnt+1))
            visited[r][c][nd]=1
            

if __name__=="__main__":
    m, n = map(int,input().split())#세로 가로 
    rect=[]
    for _ in range(m):
        rect.append(list(map(int,input().split())))
    
    sr, sc, sd = map(int,input().split())
    ar, ac, ad = map(int,input().split())
    print(bfs())
    
