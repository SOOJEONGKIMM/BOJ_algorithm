#10164_격자상의경로
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
#N:행, M:열 (상하반전)
def dp_search(y,x):
    dp = [[0 for _ in range(x+1)] for _ in range(y+1)]

    for i in range(1, y+1):
        for j in range(1, x+1):
            if i==1 and j==1:
                dp[i][j]=1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[y][x]

if K==0:
    print(dp_search(N,M))
else:
    #K의 (y,x)좌표 구하기
    k_y = (K+1) // (M-1)
    k_x = K % M
    #print(k_y, k_x)
    k_n = N - (k_y - 1)
    k_m = M - (k_x - 1)
    #print(k_n, k_m)
    route_a = dp_search(k_y, k_x)
    route_b = dp_search(k_n, k_m)

    print(route_a * route_b)
