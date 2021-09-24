#10816

import sys
input = sys.stdin.readline

N = input()
real_card = list(map(int, input().split()))
real_card.sort()

M = input()
pred_card = list(map(int, input().split()))

match = {}
for i in real_card:
    if i in match:
        match[i] += 1
    else:
        match[i] = 1
    print("match{0}={1}".format(i,match[i]))

for j in pred_card:
    if j in match:
        print(match[j], end=' ')
    else:
        print(0, end=' ')
        
