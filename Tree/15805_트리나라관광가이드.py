#15805_트리나라관광가이드
from collections import Counter
n=int(input())
city=list(map(int,input().split()))
cntcity=Counter(city)
visited=[0 for _ in range(len(cntcity.keys()))]

parent=[0 for _ in range(len(cntcity.keys()))]
parent[city[0]]=-1

tree=[city[0]]
for i in range(n):

    if visited[city[i]]==0:
        if i<=0:
            parent[city[i]]=-1
        else:
            parent[city[i]]=city[i-1]
        tree.append(city[i])
        visited[city[i]]=1


print(len(cntcity.keys()))
for i in parent:
    print(i, end=' ')
