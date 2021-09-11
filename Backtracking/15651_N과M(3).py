#15651 N과M(3)
import sys
from itertools import product
input = sys.stdin.readline

N,M = map(int, input().split())


P = product([str(i) for i in range(1, N+1)], repeat=M)

for num in P:
    print(' '.join(map(str,num)))
     
