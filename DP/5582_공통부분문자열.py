#5582_공통부분문자열
#DP, string
s = input().rstrip()
o = input().rstrip()
'''메모리 초과 ㅠㅠ O(N^2)
dp = [[0]*(len(s)+1) for _ in range(len(o)+1)]
#dp
for i in range(1, len(o)+1):
    for j in range(1, len(s)+1):
        if o[i-1]==s[j-1]:
            dp[i][j]=dp[i-1][j-1]+1


print(max(map(max, dp)))
'''

la = len(s)
lo = len(o)
prev = [0]*(lo+1)
ans=0

for i in range(la):
    tmp=[0]*(lo+1)
    for j in range(lo):
        if s[i]==o[j]:
            tmp[j+1]=prev[j]+1

    ans=max(ans,max(tmp))
    prev=tmp[:]

print(ans)
