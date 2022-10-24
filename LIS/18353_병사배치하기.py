#18353
import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))



dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] < a[j]: #감소하는 부분수열 
            dp[i] = max(dp[i], dp[j]+1)


print(len(a) -  max(dp))
