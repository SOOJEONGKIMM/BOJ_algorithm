#20364_부동산다툼
import sys
n,q=map(int,sys.stdin.readline().split())
vis=set()
for _ in range(q):
    x = int(sys.stdin.readline().rstrip())

    ans = 0
    tmp = x
    while tmp>0:
        if tmp in vis:
            ans = tmp
        tmp //= 2
    if ans==0:
        vis.add(x)#owned
    
    print(ans)
