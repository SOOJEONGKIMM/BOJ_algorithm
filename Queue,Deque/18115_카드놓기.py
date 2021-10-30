#18115_카드놓기
from collections import deque
N = int(input())
A=deque(map(int, input().split()))
stack=deque(range(1,N+1))
res=deque() #initial card
while A:
    i = A.pop()

    if len(stack)>0:
        after = stack.popleft()

        if i==1:
            res.appendleft(after)

        elif i==2:
            res.insert(1,after)

        elif i==3:
            res.append(after)
print(*res)
        
