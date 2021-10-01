#1325_효율적인 해킹
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q= deque()
    q.append(start)
    visited[start]=1
    
    while q:
        print(visited)
        start = q.popleft()
        for i in rel[start]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)

N, M = map(int, input().split())

rel = [[0] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    rel[b].append(a)

cnt = []
for i in range(1,N+1):
    visited = [0 for _ in range(N+1)] #init evry/time
    bfs(i)

    cnt.append(visited.count(1))

idx = 1
for i in cnt:
    if i==max(cnt):
        print(idx, end=" ")
    idx += 1
