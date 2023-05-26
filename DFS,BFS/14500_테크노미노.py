#14500_테크노미노
N,M = map(int,input().split())
paper=[]
for _ in range(N):
    paper.append(list(map(int,input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=0

visited=[[False]*M for _ in range(N)]
def dfs(x,y,depth,total):
    global ans
    
    if depth==3: #마지막 모양 완성
        ans = max(ans, total)        
        return
    
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
                if depth==1:#'ㅗ'모양 예외처리. 새로운 블록이 아닌 기존블록에서  dfs
                    visited[nx][ny]=True
                   
                    dfs(x,y,depth+1, total+paper[nx][ny])
                    visited[nx][ny]=False
                visited[nx][ny]=True
                dfs(nx,ny,depth+1,total+paper[nx][ny])
                visited[nx][ny]=False
            
            

for i in range(N):
    for j in range(M):
        visited[i][j]=True
        dfs(i,j,0,paper[i][j])
        visited[i][j]=False


print(ans)
