#3052_나머지
from collections import Counter
left=[]
for _ in range(10):
    num=int(input())
    left.append(num % 42)

left.sort()

cnt = Counter(left)
print(cnt)
print(len(cnt))
