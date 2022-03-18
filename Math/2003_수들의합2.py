#2003_수들의합2
n,m=map(int,input().split())
a=list(map(int,input().split()))
i,j=0,0
cnt=0
while i<n and j<n:
    if sum(a[i:j+1])<m:
        j+=1
    elif sum(a[i:j+1])==m:
        cnt+=1
        if i>j:
            i-=1
        else:
            j-=1
    else:
        i+=1
print(cnt)
