#14501_퇴사
n = int(input())
tp=[]
for _ in range(n):
    tp.append(list(map(int,input().split())))

dp = [0 for i in range(n+1)]

for i in range(n):
    for j in range(i+tp[i][0], n+1):
        dp[j] = max(dp[j], dp[i]+tp[i][1])


print(dp[-1])
        
