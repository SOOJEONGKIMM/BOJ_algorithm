#4796_캠핑
import sys
input = sys.stdin.readline
casenum=0
while(1):
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V==0:
        break
    casenum+=1
    rem=V%P
    if L < rem:
        rem = L
    vac = (V//P)*L + rem
    print("Case %d: %d"%(casenum,vac))
    
