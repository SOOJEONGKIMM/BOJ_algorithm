#18352_특정거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = list(map(int,input().split()))
    graph[a].append(b) #단방향 

visited = [-1]*(N+1) 
q = deque([X])
visited[X]=0

while q: #bfs search
    cur = q.popleft()
    for i in graph[cur]:
        if visited[i]==-1:
            visited[i] = visited[cur]+1
            q.append(i)
      
flag = 0
for i in range(N+1):
    if visited[i]==K:
        print(i)
        flag = 1
        
if flag==0:
    print("-1")
