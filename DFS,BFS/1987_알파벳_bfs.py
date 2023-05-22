#1987_알파벳
from collections import deque
r,c= map(int,input().split())
horse = []
for _ in range(r):
    horse.append(list(input().strip()))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q = set([(0,0,horse[0][0])])
cnt=1
while q:
    x,y,z=q.pop()
    cnt = max(cnt, len(z))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and horse[nx][ny] not in z:
            
            q.add((nx,ny,horse[nx][ny]+z))
            

print(cnt)
