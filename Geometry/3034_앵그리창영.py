#3034_앵그리창영
import math
n,w,h=map(int,input().split())

for _ in range(n):
    s=int(input())

    diag=math.sqrt(w**2+h**2)
    if diag < s:
        print('NE')
    else:
        print('DA')
