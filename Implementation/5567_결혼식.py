#5567_결혼식
n=int(input())
m=int(input())
friend=[]
weight={}

for _ in range(m):
    a,b = map(int, input().split())
    if a not in weight:
        weight[a]=[]
    if b not in weight:
        weight[b]=[]
    weight[a].append(b)
    weight[b].append(a)

if 1 not in weight:
    print(0)
else:


    cnt=[]
    for fr in weight[1]:
        cnt.append(fr)
        for i in weight[fr]:
            cnt.append(i)
    cnt=set(cnt)

    print(len(cnt)-1)

