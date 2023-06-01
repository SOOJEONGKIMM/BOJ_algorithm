#14501_퇴사
n=int(input())
tp = [list(map(int,input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+tp[i][0], n+1):
        dp[j]= max(dp[j], tp[i][1]+dp[i])

print(dp[-1])
