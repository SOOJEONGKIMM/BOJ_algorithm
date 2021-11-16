#1654_랜선자르기
import sys
k,n=map(int,input().split())

lan=[]
for _ in range(k):
    lan.append(int(sys.stdin.readline()))

left=1
right=max(lan)

res=0
while left <= right:
    mid=(left+right)//2

    cnt=0
    for i in lan:
        cnt += i//mid

    if cnt>=n:
        res=mid
        left=mid+1
    else:
        right=mid-1
print(res)
