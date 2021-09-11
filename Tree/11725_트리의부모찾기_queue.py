#11725_queue
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

tree= [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0 for _ in range(N+1)]#visited
queue=[1]#start from root

while queue:
    child = queue.pop(0)
    for i in tree[child]:
        if parent[i]==0:
            parent[i]=child #update parent
            queue.append(i)

for i in range(2, N+1):
    print(parent[i])
