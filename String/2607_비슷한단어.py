
#2607
from collections import Counter
n=int(input())
match=str(input())
match_c = Counter(match)
step=[]

ans=0
for _ in range(n-1):
    step_c = Counter(str(input()))
    tmp1=0
    tmp2=0
    for k in (match_c | step_c).keys():
        if match_c[k] < step_c[k]:
            tmp1 += (step_c[k] - match_c[k])
        elif match_c[k] > step_c[k]:
            tmp2 += (match_c[k] - step_c[k])

    if tmp1<=1 and tmp2<=1:
        ans+=1

print(ans)
