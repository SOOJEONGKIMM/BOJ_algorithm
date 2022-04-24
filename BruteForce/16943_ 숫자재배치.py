#16943_숫자재배치
import sys
import itertools
a,b = map(int, sys.stdin.readline().split())

num=[]
for i in range(len(str(a))):
    num.append(str(a)[i])
nPr = itertools.permutations(num,len(num))
l_npr = list(nPr)

lst = list(map(''.join, l_npr))

res = -1
for i in lst:
    
    if b >= int(i) and i[0]!='0':
        res = max(res, int(i))

print(res)
