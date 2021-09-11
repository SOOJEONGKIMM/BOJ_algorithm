#15652 N과M(4)
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M =map(int, input().split())

C = combinations_with_replacement([i for i in range(1, N+1)], M)

for num in C:
    print(' '.join(map(str,num)))
