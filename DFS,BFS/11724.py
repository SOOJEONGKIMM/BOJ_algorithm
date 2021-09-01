import sys

sys.setrecursionlimit(10000)


node, edge = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(node+1)]

visited = [False for _ in range(node+1)]

for _ in range(edge): #making graph
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    graph[n1].sort()
    graph[n2].sort()

    
def DFS(graph, visited, node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            DFS(graph,visited,i)



comp = 0


for i in range(1,node+1):
    if visited[i] == False:
        DFS(graph,visited,i)
        comp += 1
        
sys.stdout.write(str(comp))
