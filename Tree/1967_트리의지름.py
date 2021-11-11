#1967_트리의 지름
from collections import deque
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(1,n):
    parent, child, weight = map(int, input().split())
    tree[parent].append([weight, child])
    tree[child].append([weight, parent])

def bfs(node):
    queue=deque()
    queue.append([0,node])
    visited=[0]*n
    visited[node-1]=1

    diameter=[0,0]

    while queue:
        cnt, cur = queue.popleft()
        for i in tree[cur]:
            wei_val, nextt = i[0], i[1]
            if visited[nextt-1]==0:
                visited[nextt-1]=1
                queue.append((cnt+wei_val, nextt))

                if diameter[0] < cnt+wei_val:
                    diameter[1] = nextt
                    diameter[0] = cnt+wei_val

    return diameter

parent = bfs(1)
child = bfs(parent[1])
print(child[0])
                
