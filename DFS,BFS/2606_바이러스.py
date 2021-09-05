import sys
input = sys.stdin.readline

node = int(input())
graph = [[0] for _ in range(node+1)]
visited = [0 for _ in range(node+1)]
C = int(input())

for i in range(C):#making graph
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

cnt=0  
def DFS(graph, visited, node):
    visited[node] = 1
    global cnt
    for i in graph[node]:
        if visited[i]==0:
            DFS(graph, visited, i)
            cnt+=1

DFS(graph, visited, 1)
'''
for i in range(1, node+1):
    if visited[i] == 0:
        DFS(graph, visited, i)
'''
print(cnt-1)
