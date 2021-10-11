#1940_주몽
import sys
input = sys.stdin.readline
N=int(input())
M=int(input())
nums=list(map(int,input().split()))
nums.sort()
start,end=0, N-1

res=0
while start<end:
    if nums[start]+nums[end]==M:
        res+=1
        end-=1
    elif nums[start]+nums[end]<M:
        start+=1
    elif nums[start]+nums[end]>M:
        end-=1
    
print(res)
