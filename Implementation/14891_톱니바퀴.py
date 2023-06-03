#14891_톱니바퀴
from collections import deque
t = [deque(list(map(int,input().rstrip()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    r=[]
    for i in range(4):
        r.append([t[i][-2], t[i][2]])

    n, d = map(int,input().split())
    n = n-1

    if n!=0:
        for i in range(n,0,-1):
            if r[i][0]!=r[i-1][1]:
                if (n-(i-1))%2==0:
                    t[i-1].rotate(d)
                elif (n-(i-1))%2!=0:
                    t[i-1].rotate(-1*d)
            elif r[i][0]==r[i-1][1]:
                break
    if n!=3:
        for i in range(n, 3):
            if r[i][1]!=r[i+1][0]:
                if (n-(i+1))%2==0:
                    t[i+1].rotate(d)
                elif (n-(i+1))%2!=0:
                    t[i+1].rotate(-1*d)
            elif r[i][1]==r[i+1][1]:
                break
    t[n].rotate(d)

res=0
if t[0][0]==1:
    res+=1
if t[1][0]==1:
    res+=2
if t[2][0]==1:
    res+=4
if t[3][0]==1:
    res+=8

print(res)
