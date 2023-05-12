#14226_이모티콘
from collections import deque
n = int(input())
visited = [[-1]*(n+1) for _ in range(n+1)]

q = deque([(1,0)])
visited[1][0]=0
while q:
    s, c = q.popleft()
    if visited[s][s]==-1: #not visited
        visited[s][s] = visited[s][c]+1
        q.append([s,s])
    if s+c<=n and visited[s+c][c]==-1:
        visited[s+c][c]=visited[s][c]+1
        q.append([s+c,c])
    if s-1>=0 and visited[s-1][c]==-1:
        visited[s-1][c]=visited[s][c]+1
        q.append([s-1,c])

answer = -1
for i in range(n+1):
    if visited[n][i]!=-1:
        if answer == -1 or answer > visited[n][i]:
            answer = visited[n][i]

print(answer)
