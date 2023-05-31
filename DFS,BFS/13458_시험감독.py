#13458_시험감독
N=int(input())
a = list(map(int,input().split()))
b,c=map(int,input().split())

cnt=0
for i in a:
    i-=b
    cnt+=1
    if i>0:
        cnt += int(i/c)
        if i%c>0:
            cnt+=1
            
print(cnt)
