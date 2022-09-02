from collections import deque
  2 import sys
  3 a, b = map(int,sys.stdin.readline().split())
  4 
  5 q = deque([(a,1)])
  6 while q:
  7     num, cnt = q.popleft()
  8     if num==b:
  9         print(cnt)
 10         exit(0)
 11     if num <= b//2:
 12         q.append((num*2, cnt+1))
 13     if int(str(num)+'1')<=b:
 14         q.append((int(str(num)+'1'),cnt+1))
 15 
 16 print(-1)
~             
