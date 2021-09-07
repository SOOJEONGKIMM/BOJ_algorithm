import sys
from itertools import combinations
input=sys.stdin.readline

arr = []
N = int(input())

for i in range (N):
    arr.append(list(map(int,input().split())))

num_list = [i for i in range(N)]
output = 100 + 100 
for cases_start in (combinations(num_list, N//2)):
    start=0
    link=0
    for i in cases_start:
        for j in cases_start:
            start += arr[i][j]
    cases_link = [i for i in range(N) if i not in cases_start]
    for i in cases_link:
        for j in cases_link:
            link += arr[i][j]
    output = min(output, abs(start-link))
print(output)
