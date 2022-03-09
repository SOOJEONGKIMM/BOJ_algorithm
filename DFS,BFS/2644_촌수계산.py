#2644_촌수계산
import sys
#sys.setrecursionlimit()
def dfs(x):
    for i in graph[x]:
        if check[i]==0:
            check[i]=check[x]+1
            dfs(i)
n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())

    graph[x].append(y)
    graph[y].append(x)
check=[0]*(n+1)
dfs(a)
if check[b]>0:
    print(check[b])
else:
    print(-1)
