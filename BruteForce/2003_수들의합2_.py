#2003_수들의합2
i=j=0
n, m= map(int,input().split())
nums=list(map(int,input().split()))
cnt=0
while i<n and j<n:
    if sum(nums[i:j+1])<m:
        j+=1
    elif sum(nums[i:j+1])==m:
        cnt+=1
        if i<j:
            i+=1
        else:
            j+=1
    else:
        i+=1


print(cnt)
