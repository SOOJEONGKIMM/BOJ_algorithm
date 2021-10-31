#4386_별자리만들기
import math
n=int(input())
parent=[0] 
def find_parent(parent, x):
    if parent[x]!=x:
        #recur until finding root node
        return find_parent(parent, parent[int(x)])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#init parent node
for i in range(1, n+1):
    parent.append(i)
graph=[]
floatarr=[]
#union 연산 각각 수행     
for _ in range(n):
    x, y = map(float, input().split())
    weight = abs(x - y)
    floatarr.append((x,y))
for i in range(n - 1):
    for j in range(i + 1, n):
        graph.append((i,j,(math.sqrt((floatarr[i][0] - floatarr[j][0])**2 + (floatarr[i][1] - floatarr[j][1])**2))))

   # graph.append((x,y,weight))
graph.sort(key=lambda x: x[2]) #sort by weight 
tree_edges=0
mst_cost=0
while True:
    if tree_edges == n-1:
        break
    u,v,wt = graph.pop(0)
    root1 = find_parent(parent,u)
    root2 = find_parent(parent,v)
    if str(root1) != str(root2): #if u & v are in different groups
        union_parent(parent, u, v)
        mst_cost+=wt
        tree_edges+=1
print(round(mst_cost,2))
