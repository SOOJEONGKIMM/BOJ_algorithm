#1068_트리
def dfs(p, e):
    p[e] = -2 #del_node
    for i in range(len(p)):
        if e==p[i]:
            dfs(p, i)
    
n=int(input())
parent = list(map(int, input().split()))
erase = int(input())

    
dfs(parent, erase)
res=0
for i in range(len(parent)):
    if parent[i]!=-2 and i not in parent:
        res+=1

print(res)
