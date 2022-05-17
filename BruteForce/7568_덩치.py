#7568  덩치
import sys
n=int(sys.stdin.readline())

human=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#for i in range(n):
#    human[i].append(i)#index
#human.sort(key=lambda x: x[0],reverse=True)

for i in human:
    rank=1
    for j in human:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1

    print(rank, end=" ")

