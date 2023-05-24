#11558_TheGameofDeath

def dfs(node,N):
    for i in a[node]:
        if visited[i]==0:
            visited[i]=visited[node]+1
            dfs(i,N)
            
            
T=int(input())

for _ in range(T):
    
    N=int(input())
    a=[[] for _ in range(N+1)]
    for i in range(1,N+1):
        a[i].append(int(input()))

    visited=[0]*(N+1)
    dfs(1,N)
    if visited[N] > 0:
        print(visited[N])
    else:
        print(0)
