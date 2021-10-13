#9934_완전이진트리
import sys
input = sys.stdin.readline

K=int(input())
tree = list(map(int,input().split()))
bin_tree = [[] for _ in range(K)]

def binary_search(tree,depth):
    if len(tree)==1:#last layer
        bin_tree[depth].extend(tree)
        return 
    mid = len(tree) // 2
    bin_tree[depth].append(tree[mid])
    binary_search(tree[:mid],depth+1)
    binary_search(tree[mid+1:],depth+1)

binary_search(tree,0)

for i in range(K):
    if i==0:
        print(bin_tree[i][0])
    else:
        print(*bin_tree[i])
