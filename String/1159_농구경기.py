#1159_농구경기
from collections import Counter
n=int(input())
names,first=[],[]
for i in range(n):
    names.append(input())
    first.append(names[i][0])
c=Counter(first)

sortin=[]
for key, val in dict(c).items():
    if val >= 5:
        sortin.append(key)
sortin.sort()

if len(sortin)==0:
    print("PREDAJA")
else:
    for i in sortin:
        print(i,end="")
