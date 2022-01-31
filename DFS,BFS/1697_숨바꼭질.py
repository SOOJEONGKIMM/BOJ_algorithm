#1697_숨바꼭질
from collections import deque

def bfs(start, dest, visited):
    queue=deque()
    queue.append(start)

    visited[start]=0

    while queue:
        v=queue.popleft()
        if v==dest:           
            print(visited[dest])
            break
        for next_v in [v-1,v+1,v*2]:
            
            if 0<=next_v<=MAX and visited[next_v]==-1:
                visited[next_v] = visited[v]+1
                queue.append(next_v)
        


MAX=10**5
start, dest=map(int,input().split())
visited=[-1 for i in range(MAX+1)]

bfs(start,dest, visited)
