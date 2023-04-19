
#1759_암호만들기
from itertools import combinations

L, C = map(int, input().split())

char = list(sorted(map(str, input().split())))
vowel = ['a','e','i','o','u']
comb = list(combinations(char, L))
v_comb=[]
for i in comb:
    cnt=0
    for j in i:
        if j in vowel:
            cnt+=1
    if cnt>=1 and L-cnt >=2:
        v_comb.append(i)

#for c in comb:
#    sorted_comb.append(tuple(sorted(c, key=lambda x: x)))

v_comb.sort(key=lambda x:x[0:])

for s in v_comb:
    for j in s:
        print(j, end="")
    print()

