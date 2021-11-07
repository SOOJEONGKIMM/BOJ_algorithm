#18258_큐2
import sys
from collections import deque
inp = sys.stdin.readline
n=int(input())
q=deque([])

for i in range(n):
    order = inp().split()
    if order[0]=="push":
        q.append(order[1])
    elif order[0]=="front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif order[0]=="back":
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif order[0]=="pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif order[0]=="size":
        print(len(q))
    elif order[0]=="empty":
        if not q:
            print(1)
        else:
            print(0)
