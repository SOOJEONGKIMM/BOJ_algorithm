import sys
input = sys.stdin.readline

xx=[]
for _ in range(7):
    x = int(input())
    if x % 2 != 0:
        xx.append(x)

if xx:
    print(sum(xx))
    print(min(xx))
else:
    print(-1)
