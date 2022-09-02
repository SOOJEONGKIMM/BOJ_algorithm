from collections import deque
import sys
a, b = map(int,sys.stdin.readline().split())

q = deque([(a,1)])
while q:
    num, cnt = q.popleft()
    if num==b:
	print(cnt)
	exit(0)
    if num <= b//2:
	q.append((num*2, cnt+1))
    if int(str(num)+'1')<=b:
	q.append((int(str(num)+'1'),cnt+1))
    
print(-1)
