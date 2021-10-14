#5639_이진검색트리
import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

def postorder(left,right):
    if left > right:
        return
    else:
        root=preorder[left]
        div = right+1
        for i in range(left+1,right+1):
            if root<preorder[i]: 
                div = i
                break
        postorder(left+1, div-1)
        postorder(div, right)
        print(root)
    
preorder=[]
while True:
    try:
        preorder.append(int(input()))
    except:
        break

postorder(0,len(preorder)-1)
