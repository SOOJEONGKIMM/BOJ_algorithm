#15654_N 과 M(5)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

visited = [0]*N
perm=[]
def dfs(n):
    if n==M:
        print(*perm)
        return
    
    for i in range(N):
        if visited[i]:
            continue;
        perm.append(nums[i])
        visited[i]=1
        dfs(n+1)
        perm.pop()
        visited[i]=0
dfs(0)
