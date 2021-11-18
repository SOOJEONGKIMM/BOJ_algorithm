#18222_투에-모스문자열
import sys
import math
sys.setrecursionlimit(10**6)
k=int(sys.stdin.readline())

def tm(n,k,cnt):
    if k==1:
        return 0, cnt
    elif k==2:
        return 1, cnt
    #k를 절반으로 나누었을때 2^n
    elif 0<=2**(n-1)-k:
        return tm(n-1,k,cnt)
    elif k>2**(n-1):
        return tm(n-1,k-2**(n-1),cnt+1)


n=math.ceil(math.log(k,2))
num, cnt = tm(n,k,0)

if cnt % 2==0:
    print(num)
else:
    if num==1:
        print(0)
    else:
        print(1)
