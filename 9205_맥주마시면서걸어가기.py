#9205_맥주마시면서걸어가기
from collections import deque
import math
def bfs():
    q=deque()
    q.append([home[0],home[1]])
    while q:
        x, y=q.popleft()
        dest = abs(x - fest[0]) + abs(y - fest[1])
        print(dest)
        if dest <= 1000:
            return "happy"
        else:
            for i in range(n):
                if visited[i]!=1:
                    
                    #dest -= 1000
                    x, y=conv[i]
                    if abs(x - fest[0]) + abs(y - fest[1]) <=1000:
                        q.append(conv[i])
                        visited[i]=1
    return "sad"
                    
t=int(input())
for _ in range(t):
    n=int(input())
    home=list(map(int,input().split()))
    conv=[]
    for i in range(n):
        conv.append(list(map(int,input().split())))
    fest = list(map(int,input().split()))
    visited=[0 for i in range(n+1)]

    print(bfs())
