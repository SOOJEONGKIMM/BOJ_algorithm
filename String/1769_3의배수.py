#1769_3의배수
import sys
input = sys.stdin.readline
X = list(map(int,input().rstrip()))
cnt=0

while(1):
    if len(X)==1:
        print(cnt)

        if int(X[0]) in [3,6,9]:
            print("YES")
            break
        else:
            print("NO")
            break
    X=list(map(int,str(sum(X))))
    cnt+=1
