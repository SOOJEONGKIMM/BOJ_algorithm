#2531_회전초밥
from collections import defaultdict
n,d,k,c = map(int,input().split())
roll=[]
for _ in range(n):
    roll.append(int(input()))


left=0
right=0
d = defaultdict(int)
result = 0

while right < k:
    d[roll[right]] +=1
    right+=1

d[c] += 1

while left < n:
    result = max(result, len(d))
    d[roll[left]]-=1
    if d[roll[left]]==0:
        del d[roll[left]]
    d[roll[right%n]]+=1
    right+=1
    left+=1

print(result)
