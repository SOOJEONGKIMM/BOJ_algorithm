#로봇조종하기
#dp
n, m = map(int,input().split())
dp = [list(map(int,input().split())) for _ in range(n)]

#dp 테이블 첫번째 행 업뎃
for j in range(1, m):
    dp[0][j] += dp[0][j-1]


for i in range(1, n):
    left_to_right = dp[i][:]
    right_to_left = dp[i][:]

    #왼쪽에서 오른쪽 업데이트 
    for j in range(m):
    
        if j==0:
            #위쪽에서 오는거만 있음 
            left_to_right[j] += dp[i-1][j]
        else:
            #왼쪽에서 오는거랑 위에서 오는거 비교 
            left_to_right[j] += max(dp[i-1][j], left_to_right[j-1])

    #오른쪽에서 왼쪽 업데이트
    for j in range(m-1, -1, -1):
        if j==m-1:
            right_to_left[j] += dp[i-1][j]
        else:
            right_to_left[j] += max(dp[i-1][j], right_to_left[j+1])

    for j in range(m):
        dp[i][j] = max(left_to_right[j], right_to_left[j])


    
print(dp[n-1][m-1])
