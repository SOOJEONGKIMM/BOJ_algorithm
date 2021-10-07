#1009_분산처리
import sys
input = sys.stdin.readline
T = int(input())
A=[]
B=[]
for _ in range(T):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

for i in range(T):
    one = A[i] % 10

    if one == 0:
        print(10)
    elif one in [1,5,6]:
        print(one)
    elif one in [4,9]:
        if B[i]%2 == 0:
            print(one ** 2 % 10)
        else:
            print(one)
    else:
        if B[i]%4==0:
            print(one ** 4 % 10)
        else:
            print(one ** (B[i] % 4) % 10)
