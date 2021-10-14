#1991_트리순회
import sys
input = sys.stdin.readline

N = int(input())


def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])#left
        preorder(tree[root][1])#right

def inorder(root): #중위
    if root!='.':
        inorder(tree[root][0])#left
        print(root,end='')
        inorder(tree[root][1])#right

def postorder(root):#후위
    if root!='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end='')

tree={}
for _ in range(N):
    root, left, right = input().strip().split()
    tree[root]=[left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
