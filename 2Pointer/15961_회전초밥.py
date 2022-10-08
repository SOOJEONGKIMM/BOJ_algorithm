#2531_회전초밥
from collections import defaultdict 
n,d,k,c = map(int,input().split())
roll=[]
for _ in range(n):
    roll.append(int(input()))

roll.extend(roll)
d = defaultdict(int)
right,left=0,0

while right < k:
     d[roll[right]]+=1
     right+=1
d[c]+=1
answer=0
while right < len(roll):
    answer = max(answer, len(d))
    #왼쪽 초밥 제거 
    d[roll[left]]-=1
    if d[roll[left]]==0:
        del d[roll[left]]
    d[roll[right]]+=1
    left+=1
    right+=1


print(answer)
