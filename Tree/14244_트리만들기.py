#14244_트리만들기
n, m = map(int, input().split())
 
# 리프의 개수
leaf = 0
if m == 2:
    leaf = 1  # 중심 노드를 리프로 포함
 
last_leaf = 0
flag=True
for i in range(1, n):
    if m > leaf:
        if flag==True:
            print(0, i)
            flag=False
        else:
            print(1,i)
        leaf += 1
    else:
        print(last_leaf, i)
    last_leaf = i
