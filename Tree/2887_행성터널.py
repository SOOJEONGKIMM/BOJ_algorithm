#2887_행성터널
N=int(input())
def find_parent(parent, x):
    if parent[x]!=x:
        #recur until finding root node
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
parent=[0]
for i in range(1, N+1):
    parent.append(i)
tmp=[]
for i in range(N):
    x,y,z = map(int,input().split())
    tmp.append([x,y,z,i]) #i번째 노드 
graph=[]
for j in range(3):
    tmp.sort(key=lambda x: x[j]) #각 좌표별로 정렬
    before_loc = tmp[0][3]
    for i in range(1,N):
        cur_loc = tmp[i][3]
        graph.append([abs(tmp[i][j]-tmp[i-1][j]),before_loc,cur_loc])
        before_loc = cur_loc
graph.sort(key=lambda x: x[0])


tree_edges=0
mst_cost=0
for wt, u, v in graph:
    if tree_edges == N-1:
        break
    if find_parent(parent,u) != find_parent(parent,v): #if u & v are in different groups
        mst_cost+=wt
        union_parent(parent, u, v)
print(mst_cost)
