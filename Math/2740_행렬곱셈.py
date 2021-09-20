#2740_행렬곱셈
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A_element = []
for _ in range(N):
    A_element.append(list(map(int,input().split())))

M, K = map(int, input().split())
B_element = []
for _ in range(M):
    B_element.append(list(map(int,input().split())))

tmp_el=0
tmp=[]
res = []
for i in range(N):
    for j in range(K):
        for a in range(M):
            tmp_el += A_element[i][a]*B_element[a][j]
        tmp.append(tmp_el)
        tmp_el = 0
    res.append(tmp)
    tmp = []

for i in res:
    for j in i:
        print(j, end=' ')
    print()
