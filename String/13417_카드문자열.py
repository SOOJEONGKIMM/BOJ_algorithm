#13417_카드문자열
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    res=[]
    N = int(input())
    card = deque(input().split())
    res.append(card.popleft())

    while card:
        compare = card.popleft()
        if compare > res[0]:
            res.append(compare)
        else:
            res.insert(0,compare)
    print(''.join(res))

