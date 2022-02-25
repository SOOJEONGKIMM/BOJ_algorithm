#4803_트리
import sys
def bfs(x):#search if cycle or not(isTree)
    isTree=True
    node=[x]
    while node:
        cur = node.pop(0)
        if visited[cur]==1:
            isTree=False
        visited[cur]=1
        for i in graph[cur]:
            if visited[i]==0:
                node.append(i)
    return isTree
    

cnt=0
while True:
    cnt+=1
    n,m = map(int,sys.stdin.readline().split())
    if n==0 and m==0:
        break
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    treecnt=0
    visited=[0]*(n+1)
    for i in range(1,n+1):
        if visited[i]==0:
            if bfs(i)==True:
                treecnt+=1
    if treecnt==0:
        print("Case {}: No trees.".format(cnt))
    elif treecnt==1:
        print("Case {}: There is one tree.".format(cnt))
    else:
        print("Case {}: A forest of {} trees.".format(cnt,treecnt))
            
    
