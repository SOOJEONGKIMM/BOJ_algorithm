#6603_로또
from itertools import combinations
import sys
while True:
    lotto=list(map(str,input().split()))
    if lotto[0]=='0':
        break
    else:
        k=lotto[0]
        lotto=lotto[1:]
        for i in combinations(lotto,6):
            print(" ".join(i))
    print()
