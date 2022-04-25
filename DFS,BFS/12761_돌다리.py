#12761_돌다리
from collections import deque
a,b,n,m = map(int, input().split())

def bfs(node):
    q=deque()
    q.append(node)
    graph[node]=0
    while q:
        node = q.popleft()
        for i in [node-1, node+1, node+a, node-a, node+b, node-b, node*a, node*b]:
            if (0<=i<=100000) and graph[i]==-1:
                q.append(i)
                graph[i]=graph[node]+1
                if i == m:
                    return graph[m]


graph = [-1]*100001
print(bfs(n))
