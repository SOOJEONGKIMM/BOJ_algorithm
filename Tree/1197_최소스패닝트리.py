#1197 MST
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

kruskal = []
for i in range(E):
    a, b, w = map(int, input().split())
    kruskal.append((a,b,w))

kruskal.sort(key=lambda x: x[2]) #sort by weight

parent = [i for i in range(V+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


weight_sum=0
for a,b,w in kruskal:

    if find(a)!=find(b):
        
        a = find(a)
        b = find(b)

        if a > b:
            parent[a] = b
        else:
            parent[b] = a

        weight_sum += w

print(weight_sum)
        
    
