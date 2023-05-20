#14889_스타트와 링크
from itertools import combinations
n = int(input())
s=[]
for _ in range(n):
    s.append(list(map(int,input().split())))

num_list = [i for i in range(n)]
output = 100 + 100

for cases_start in combinations(num_list, n//2):
    start=0
    link=0
    #print('start',cases_start)
    for i in cases_start:
        for j in cases_start:
            #print(i,j)
            start+=s[i][j]

    cases_link = [i for i in range(n) if i not in cases_start]
    #print('link',cases_link)
    for i in cases_link:
        for j in cases_link:
            link+=s[i][j]

    #print(start, link, start-link)
    output = min(output, abs(start-link))
    
print(output)
