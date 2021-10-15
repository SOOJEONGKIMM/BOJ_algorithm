#2563_색종이
import sys
input = sys.stdin.readline
fill = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())
for _ in range(N):
    x,y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            fill[i][j]=1

black=0
for i in fill:
    black += i.count(1)
print(black)
