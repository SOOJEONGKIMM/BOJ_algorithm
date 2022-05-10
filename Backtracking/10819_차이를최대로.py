#10819_차이를 최대로
import sys
from itertools import permutations
n=sys.stdin.readline()
a=list(map(int,sys.stdin.readline().split()))

res=0
a=permutations(a)

for i in a:
    tmp_res=0
    for j in range(len(i)-1):
        tmp_res += abs(i[j]-i[j+1])

    res = max(res, tmp_res)
       
print(res)
