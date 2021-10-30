#11051:이항계수
import sys
N, K = map(int, input().split())
sys.setrecursionlimit(2000)

triangle = [[-1] * 1001 for _ in range(1001)]


def bino_coef(N, K):
    if (K > N):
        return 0
    
    if K==0 or K==N:
        return 1
    
    if triangle[N][K] == -1:
        triangle[N][K] = (bino_coef(N-1,K-1) + bino_coef(N-1,K)) % 10007
    return triangle[N][K]

print(bino_coef(N, K))
