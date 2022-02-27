#11403_경로찾기
import sys
n=int(sys.stdin.readline())
def dfs(x):
    
    for i in range(n):
        if visited[i]==0 and adjacent[x][i]==1:
            visited[i]=1
            dfs(i)
            
adjacent=[]
for i in range(n):
    adjacent.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    visited=[0 for i in range(n)]
    dfs(i)
    for j in range(n):
        if visited[j]==1:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
