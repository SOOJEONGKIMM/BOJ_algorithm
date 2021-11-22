#9375_패션왕신해빈
import sys
from itertools import product
from itertools import combinations

n=int(input())
for _ in range(n):
    clothes={}
    
    m=int(input())
    for _ in range(m):
        
        a,b=map(str,input().strip().split())

        if b in clothes.keys():
            clothes[b]+=1
        else:
            clothes[b]=1
    res=1
    for key in clothes.keys():
        res *= clothes[key]+1               
    print(res-1)
