#11441 합 구하기
import sys
input = sys.stdin.readline

N = int(input())

A = []
A =list(map(int, input().split()))

ans = [0]*(N+1)

for k in range(N):
    ans[k] = ans[k-1]+A[k]

M = int(input())

for k in range(M):
    i, j = map(int, input().split())

    res = ans[j-1]-ans[i-2] 
    sys.stdout.write(str(res)+'\n')
  
