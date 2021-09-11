#11725_recursion
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
parent = [0 for _ in range(N+1)] #visited

def dfs(child,tree,parent):
    for i in tree[child]:
        if parent[i]==0: #unvisited
            parent[i]=child #parent update 
            dfs(i, tree, parent)

dfs(1, tree, parent)

for i in range(2, N+1):
    print(parent[i])
