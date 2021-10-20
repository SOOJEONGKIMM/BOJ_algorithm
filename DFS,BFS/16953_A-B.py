#16953_A->B
from collections import deque
A, B= map(int, input().split())

def dfs(x,y):
    q=deque([(x,y)])
    while q:
        num, cnt = q.popleft()
        if num == B:
            return cnt
        if num * 2 <= B:
            q.append((num*2, cnt+1))
        if int(str(num)+'1') <= B:
            q.append((int(str(num)+'1'), cnt+1))
    return -1
print(dfs(A,1))
        
