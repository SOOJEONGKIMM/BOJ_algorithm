#12852_1로만들기2
from collections import deque
n=int(input())
q=deque()
q.append([n])

while q:
    arr=q.popleft()
    x=arr[0]
    
    
    if x==1:
        arr = sorted(arr,reverse=True)
        break
    if x%3==0:
        q.append([x//3]+arr)

    if x%2==0:
        q.append([x//2]+arr)
    
    q.append([x-1]+arr)

print(len(arr)-1)

for i in arr:
    print(i, end=' ')
