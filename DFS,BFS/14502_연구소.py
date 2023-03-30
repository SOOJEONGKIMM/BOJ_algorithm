#14502_연구소
import copy
from collections import deque
move=[[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    queue = deque()
    test_area = copy.deepcopy(area)
    for i in range(n):
        for j in range(m):
            if test_area[i][j]==2:
                queue.append((i,j))
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            da = a + move[k][0]
            db = b + move[k][1]

            if 0<=da<n and 0<=db<m:
                if test_area[da][db]==0:
                    test_area[da][db]=2
                    queue.append((da,db))

    global result
    cnt=0
    for i in range(n):
        for j in range(m):
            if test_area[i][j]==0:
                cnt+=1
    result = max(result, cnt)
    

def make_wall(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if area[i][j]==0:
                area[i][j] = 1
                make_wall(cnt+1)
                area[i][j] = 0



n,m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]
result=0
make_wall(0)
print(result)
